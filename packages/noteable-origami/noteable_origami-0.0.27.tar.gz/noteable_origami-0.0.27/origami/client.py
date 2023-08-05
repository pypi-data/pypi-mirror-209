"""The file holding client connection patterns for noteable APIs."""

import asyncio
import functools
import uuid
from asyncio import Future
from collections import defaultdict
from queue import LifoQueue
from typing import Any, Dict, Optional, Type, Union
from uuid import UUID, uuid4

import backoff
import httpx
import structlog
import websockets
import websockets.exceptions
from httpx import ReadTimeout
from nbclient.util import run_sync
from pydantic import BaseModel, BaseSettings, ValidationError
from websockets.legacy.client import WebSocketClientProtocol

from origami.defs.deltas import NBMetadataProperties, V2CellMetadataProperties
from origami.defs.rtu import BulkCellStateMessage

from .defs.deltas import FileDeltaAction, FileDeltaType, NBCellProperties, V2CellContentsProperties
from .defs.files import FileVersion, NotebookFile
from .defs.jobs import (
    CreateParameterizedNotebookRequest,
    CreateParameterizedNotebookResponse,
    CustomerJobInstanceReference,
    CustomerJobInstanceReferenceInput,
    JobInstanceAttempt,
    JobInstanceAttemptRequest,
    JobInstanceAttemptUpdate,
)
from .defs.kernels import SessionRequestDetails
from .defs.rtu import (
    RTU_ERROR_HARD_MESSAGE_TYPES,
    RTU_MESSAGE_TYPES,
    AuthenticationReply,
    AuthenticationRequest,
    AuthenticationRequestData,
    CallbackTracker,
    FileDeltaReply,
    FileSubscribeReplySchema,
    GenericRTUMessage,
    GenericRTUReply,
    GenericRTUReplySchema,
    GenericRTURequest,
    GenericRTURequestSchema,
    KernelStatusUpdate,
    MinimalErrorSchema,
    PingReply,
    PingRequest,
    RTUEventCallable,
    TopicActionReplyData,
)

logger = structlog.get_logger('noteable.' + __name__)

EXP_BACKOFF_MAX_TIME = 60


class SkipCallback(ValueError):
    """Used to allow a message handler to gracefully skip processing and not be counted as a match"""

    pass


class RTUError(RuntimeError):
    pass


class ClientConfig(BaseSettings):
    """A pydantic settings object for loading settings into dataclasses"""

    http_protocol: str = "https"
    websocket_protocol: str = "wss"
    domain: str = "app.noteable.io"
    backend_path: str = "gate/api"
    ws_timeout: int = 60
    token: Optional[str] = None

    class Config:
        env_prefix = "noteable_"

    def __init__(
        self,
        api_token: Optional[str] = None,
        **kwargs,
    ):
        """Initializes the config and overrides api_token if it is passed in."""
        if api_token:
            kwargs["token"] = api_token
        super().__init__(**kwargs)


class NoteableClient(httpx.AsyncClient):
    """An async client class that provides interfaces for communicating with Noteable APIs."""

    def _requires_ws_context(func):
        """A helper for checking if one is in a websocket context or not"""

        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            if not self.in_context:
                raise ValueError("Cannot send RTU request outside of a context manager scope.")
            return await func(self, *args, **kwargs)

        return wrapper

    def _default_timeout_arg(func):
        """A helper for setting a default timeout on async methods."""

        @functools.wraps(func)
        async def wrapper(self, *args, timeout=None, **kwargs):
            if timeout is None:
                timeout = self.config.ws_timeout
            return await func(self, *args, timeout=timeout, **kwargs)

        return wrapper

    def __init__(
        self,
        api_token: Optional[str] = None,
        config: Optional[ClientConfig] = None,
        follow_redirects=True,
        **kwargs,
    ):
        """Initializes httpx client and sets up state trackers for async comms."""
        self.config = config or ClientConfig(api_token=api_token)

        self.user = None
        self.rtu_socket: WebSocketClientProtocol = None
        self.process_task_loop = None

        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f"Bearer {self.config.token}"

        # Set of active channel subscriptions (always subscribed to system messages)
        self.subscriptions = {'system'}
        # channel -> message_type -> callback_queue
        self.type_callbacks = defaultdict(lambda: defaultdict(LifoQueue))
        # channel -> transaction_id -> callback_queue
        self.transaction_callbacks = defaultdict(lambda: defaultdict(LifoQueue))
        super().__init__(
            base_url=f"{self.config.http_protocol}://{self.config.domain}/",
            follow_redirects=follow_redirects,
            headers=headers,
            timeout=self.config.ws_timeout,
            **kwargs,
        )

        self.reconnect_rtu_task = None

    @property
    def origin(self):
        """Formats the domain in an origin string for websocket headers."""
        return f'{self.config.http_protocol}://{self.config.domain}'

    @property
    def ws_uri(self):
        """Formats the websocket URI out of the notable domain name."""
        return f"{self.config.websocket_protocol}://{self.config.domain}/{self.config.backend_path}/v1/rtu"

    @property
    def api_server_uri(self):
        """Formats the http API URI out of the notable domain name."""
        return f"{self.config.http_protocol}://{self.config.domain}/{self.config.backend_path}"

    @_default_timeout_arg
    @backoff.on_exception(backoff.expo, ReadTimeout, max_time=EXP_BACKOFF_MAX_TIME)
    async def get_notebook(self, file_id, timeout=None) -> NotebookFile:
        """Fetches a notebook file via the Noteable REST API as a NotebookFile model (see files.py)"""
        resp = await self.get(f"{self.api_server_uri}/files/{file_id}", timeout=timeout)
        resp.raise_for_status()
        return NotebookFile.parse_raw(resp.content)

    @_default_timeout_arg
    @backoff.on_exception(backoff.expo, ReadTimeout, max_time=EXP_BACKOFF_MAX_TIME)
    async def get_version_or_none(
        self, version_id: UUID, timeout: int = None
    ) -> Optional[FileVersion]:
        """Fetches a file version via the Noteable REST API as a FileVersion model (see files.py)"""
        resp = await self.get(f"{self.api_server_uri}/fileversions/{version_id}", timeout=timeout)
        if resp.status_code == 404:
            return
        resp.raise_for_status()
        return FileVersion.parse_raw(resp.content)

    @backoff.on_exception(backoff.expo, ReadTimeout, max_time=EXP_BACKOFF_MAX_TIME)
    async def get_kernel_session(
        self, file: Union[UUID, NotebookFile]
    ) -> Optional[KernelStatusUpdate]:
        """Fetches the first notebook kernel session via the Noteable REST API.
        Returns None if no session is active.
        """
        file_id = file if not isinstance(file, NotebookFile) else file.id
        resp = await self.get(f"{self.api_server_uri}/files/{file_id}/sessions")
        resp.raise_for_status()
        resp_data = resp.json()
        if resp_data:
            session = KernelStatusUpdate(
                session_id=resp_data[0]["id"], kernel=resp_data[0]["kernel"]
            )
            return session

    @backoff.on_exception(backoff.expo, ReadTimeout, max_time=EXP_BACKOFF_MAX_TIME)
    async def launch_kernel_session(
        self,
        file: NotebookFile,
        kernel_name: Optional[str] = None,
        hardware_size: Optional[str] = None,
    ) -> KernelStatusUpdate:
        """Requests that a notebook session be launched via the Noteable REST API"""
        request = SessionRequestDetails.generate_file_request(
            file, kernel_name=kernel_name, hardware_size=hardware_size
        )
        # Needs the .dict conversion to avoid thinking it's an object with a synchronous byte stream
        resp = await self.post(f"{self.api_server_uri}/v1/sessions", content=request.json())
        resp.raise_for_status()
        resp_data = resp.json()
        session = KernelStatusUpdate(session_id=resp_data["id"], kernel=resp_data["kernel"])
        return session

    @backoff.on_exception(
        backoff.expo, asyncio.exceptions.TimeoutError, max_time=EXP_BACKOFF_MAX_TIME
    )
    async def get_or_launch_ready_kernel_session(
        self,
        file: NotebookFile,
        kernel_name: Optional[str] = None,
        hardware_size: Optional[str] = None,
        launch_timeout=60 * 10,
    ) -> KernelStatusUpdate:
        """Gets or requests that a notebook session be launched via the Noteable REST API.
        If no session is available one is created, if one is available but not ready it awaits the kernel session
        being ready for further requests.
        """
        resp = await self.subscribe_file(file)
        assert resp.data.success, "Failed to connect to the files channel over RTU"
        session = resp.data.kernel_session
        if not session:

            async def _kernel_status_callback(msg):
                return msg

            session = await self.launch_kernel_session(
                file, kernel_name=kernel_name, hardware_size=hardware_size
            )

            kernel_status_tracker = self.register_message_callback(
                _kernel_status_callback,
                channel=session.kernel_channel,
                message_type="kernel_status_update_event",
                once=False,
            )

            while session is not None and not session.kernel.execution_state.kernel_is_alive:
                kernel_status_tracker_future = kernel_status_tracker.next_trigger
                if kernel_status_tracker_future.done():
                    kernel_status_update = kernel_status_tracker_future.result()
                else:
                    kernel_status_update = await asyncio.wait_for(
                        kernel_status_tracker_future, timeout=launch_timeout
                    )
                session = KernelStatusUpdate.parse_obj(kernel_status_update.data)

        return session

    @_default_timeout_arg
    async def delete_kernel_session(self, file: Union[UUID, NotebookFile], timeout: float = None):
        """Fetches the first notebook kernel session via the Noteable REST API.
        Returns None if no session is active.
        """
        session = await self.get_kernel_session(file)
        if session is None:
            return  # Already shutdown
        resp = await self.delete(
            f"{self.api_server_uri}/sessions/{session.session_id}", timeout=timeout
        )
        resp.raise_for_status()

    @_default_timeout_arg
    async def create_parameterized_notebook(
        self,
        notebook_id: UUID,
        job_instance_attempt: JobInstanceAttemptRequest = None,
        timeout: float = None,
    ) -> CreateParameterizedNotebookResponse:
        """
        Creates a parameterized_notebook given a notebook version id or a notebook file id.

        If given a notebook version id, fetch the version details and extract file id to construct the request path.
        """
        file_version = await self.get_version_or_none(notebook_id)
        file_id = notebook_id if file_version is None else file_version.file_id
        notebook_version_id = None if file_version is None else file_version.id
        body = CreateParameterizedNotebookRequest(
            notebook_version_id=notebook_version_id, job_instance_attempt=job_instance_attempt
        )
        resp = await self.post(
            f"{self.api_server_uri}/v1/files/{file_id}/parameterized_notebooks",
            content=body.json(),
            timeout=timeout,
        )
        resp.raise_for_status()
        resp_data = resp.json()

        # Use .get(...) for backwards compatibility with old API which returns the NotebookFile as the response
        parameterized_notebook = NotebookFile.parse_obj(
            resp_data.get('parameterized_notebook', resp_data)
        )
        parameterized_notebook.content = httpx.get(
            parameterized_notebook.presigned_download_url
        ).content.decode("utf-8")
        job_instance_attempt = (
            JobInstanceAttempt.parse_obj(resp_data['job_instance_attempt'])
            if resp_data.get('job_instance_attempt')
            else None
        )

        return CreateParameterizedNotebookResponse(
            parameterized_notebook=parameterized_notebook, job_instance_attempt=job_instance_attempt
        )

    @_default_timeout_arg
    async def create_job_instance(
        self, job_instance_input: CustomerJobInstanceReferenceInput, timeout: float = None
    ) -> CustomerJobInstanceReference:
        """Create a job instance in Noteable, reference a job instance in a third-party system.

        A job definition has many job instances, a job instance has many attempts.
        Each attempt is created through the `create_parameterized_notebook` method.
        """
        resp = await self.post(
            f"{self.api_server_uri}/v1/customer-job-instances",
            content=job_instance_input.json(exclude_unset=True),
            timeout=timeout,
        )
        resp.raise_for_status()
        return CustomerJobInstanceReference.parse_obj(resp.json())

    @_default_timeout_arg
    @backoff.on_exception(backoff.expo, ReadTimeout, max_time=EXP_BACKOFF_MAX_TIME)
    async def update_job_instance(
        self,
        job_instance_attempt_id: uuid.UUID,
        job_instance_attempt_update: JobInstanceAttemptUpdate,
        timeout: float = None,
    ) -> JobInstanceAttempt:
        """Update the status of a job instance attempt by id"""
        resp = await self.patch(
            f"{self.api_server_uri}/v1/job-instance-attempts/{job_instance_attempt_id}",
            content=job_instance_attempt_update.json(exclude_unset=True),
            timeout=timeout,
        )
        resp.raise_for_status()
        return JobInstanceAttempt.parse_obj(resp.json())

    @property
    def in_context(self):
        """Indicates if the client is within an async context generation loop or not."""
        return self.rtu_socket is not None

    async def __aenter__(self):
        """
        Creates an async test client for the Noteable App.

        An Authorization Bearer header must be present or Noteable
        returns a 403 immediately. Normally that bearer token is
        JWT format and the verify_jwt_token Security function would
        validate and extract principal-user-id from the token.
        """
        res = await httpx.AsyncClient.__aenter__(self)
        # Create a new RTU socket for this context
        await self._connect_rtu_socket()
        # Loop indefinitely over the incoming websocket messages
        self.process_task_loop = asyncio.create_task(self._process_messages())
        # Authenticate for more advanced API calls
        await self.authenticate()
        return res

    async def __aexit__(self, exc_type, exc, tb):
        """Cleans out the tracker states and closes the httpx + websocket contexts."""
        try:
            if self.process_task_loop:
                self.process_task_loop.cancel()
                self.process_task_loop = None
            if self.rtu_socket:
                await self.rtu_socket.close()
                self.rtu_socket = None
            self.subscriptions = {'system'}
            # channel -> message_type -> callback_queue
            self.type_callbacks = defaultdict(lambda: defaultdict(LifoQueue))
            # channel -> transaction_id -> callback_queue
            self.transaction_callbacks = defaultdict(lambda: defaultdict(LifoQueue))
        except Exception:
            logger.exception("Error in closing out nested context loops")
        finally:
            return await httpx.AsyncClient.__aexit__(self, exc_type, exc, tb)

    def __enter__(self):
        return run_sync(self.__aenter__)()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return run_sync(self.__aexit__)(exc_type, exc_val, exc_tb)

    def register_message_callback(
        self,
        callable: RTUEventCallable,
        channel: str,
        message_type: Optional[str] = None,
        transaction_id: Optional[UUID] = None,
        once: bool = True,
        response_schema: Optional[Type[BaseModel]] = None,
    ) -> CallbackTracker:
        """Registers a callback function that will be executed upon receiving the
        given message event type or transaction id in the specified topic channel.

        Multiple callbacks can exist against each callable.

        The once flag will indicate this callback should only be used for the next
        event trigger (default True).
        """
        tracker = CallbackTracker(
            once=once,
            count=0,
            callable=callable,
            channel=channel,
            message_type=message_type,
            transaction_id=transaction_id,
            next_trigger=Future(),
            response_schema=response_schema,
        )

        async def wrapped_callable(resp: GenericRTUMessage):
            """Wraps the user callback function to handle message parsing and future triggers."""
            skipped = False
            failed = False
            if resp.event in RTU_ERROR_HARD_MESSAGE_TYPES:
                resp = MinimalErrorSchema.parse_obj(resp)
                msg = resp.data['message']
                logger.exception(f"Request failed: {msg}")
                # TODO: Different exception class?
                if not tracker.next_trigger.cancelled():
                    tracker.next_trigger.set_exception(ValueError(msg))
            else:
                if tracker.response_schema:
                    resp = tracker.response_schema.parse_obj(resp)
                elif tracker.message_type in RTU_MESSAGE_TYPES:
                    resp = RTU_MESSAGE_TYPES[tracker.message_type].parse_obj(resp)

                try:
                    if not tracker.next_trigger.cancelled():
                        result = await callable(resp)
                        tracker.count += 1
                        tracker.next_trigger.set_result(result)
                    else:
                        logger.debug("Skipped setting result due to future cancellation")
                except SkipCallback:
                    # Allow for skipping if conditions were not met
                    skipped = True
                except Exception as e:
                    logger.exception("Registered callback failed")
                    failed = True
                    tracker.count += 1
                    if not tracker.next_trigger.cancelled():
                        tracker.next_trigger.set_exception(e)
                    else:
                        # Technically this case is impossible, but keeping it here for completeness
                        logger.debug("Skipped setting exception due to future cancellation")

            if skipped or not tracker.once:
                # Reset the next trigger promise
                if not skipped:
                    tracker.next_trigger = Future()
                if tracker.transaction_id:
                    self.transaction_callbacks[tracker.channel][tracker.transaction_id].put_nowait(
                        tracker
                    )
                else:
                    self.type_callbacks[tracker.channel][tracker.message_type].put_nowait(tracker)
            return not skipped and not failed

        # Replace the callable with a function that will manage itself and it's future awaitable
        tracker.callable = wrapped_callable
        if tracker.transaction_id:
            self.transaction_callbacks[channel][transaction_id].put_nowait(tracker)
        else:
            self.type_callbacks[channel][message_type].put_nowait(tracker)
        return tracker

    async def _process_messages(self):
        """Provides an infinite control loop for consuming RTU websocket messages.

        The loop will parse the message, convert to a RTUReply or RTURequest,
        log any validation errors (skipping callbacks), and finally identifying
        any callbacks that are registered to consume the given message and pass
        the message as the sole argument.
        """
        while True:
            # Release context control at the start of each loop
            await asyncio.sleep(0)
            try:
                msg = await self.rtu_socket.recv()
                if not isinstance(msg, str):
                    logger.exception(f"Unexpected message type found on socket: {type(msg)}")
                    continue
                try:
                    res = GenericRTUReply.parse_raw(msg)
                    channel = res.channel
                    event = res.event
                except ValidationError:
                    try:
                        res = GenericRTURequest.parse_raw(msg)
                        channel = res.channel
                        event = res.event
                    except ValidationError:
                        logger.exception(
                            f"Unexpected message found on socket: {msg[:30]}{'...' if len(msg) > 30 else ''}"
                        )
                        continue

                logger.debug(f"Received websocket message: {res}")
                # Check for transaction id responses
                id_lifo = self.transaction_callbacks[channel][res.transaction_id]
                # Pull all the trackers out initially so that re-registering trackers don't get rerun this cycle
                trackers = []
                while not id_lifo.empty():
                    trackers.append(id_lifo.get(block=False))
                for tracker in trackers:
                    logger.debug(f"Found callable for {channel}/{tracker.transaction_id}")
                    processed = await tracker.callable(res)
                    logger.debug(
                        f"Callable for {channel}/{tracker.transaction_id} was a "
                        f"{'successful' if processed else 'failed'} match"
                    )

                # Check for general event callbacks
                type_lifo = self.type_callbacks[channel][event]
                # Pull all the trackers out initially so that re-registering trackers don't get rerun this cycle
                trackers = []
                while not type_lifo.empty():
                    trackers.append(type_lifo.get(block=False))
                for tracker in trackers:
                    logger.debug(f"Found callable for {channel}/{event}")
                    processed = await tracker.callable(res)
                    logger.debug(
                        f"Callable for {channel}/{event} was a {'successful' if processed else 'failed'} match"
                    )
            except websockets.exceptions.ConnectionClosed:
                await asyncio.sleep(0)
                logger.exception("Websocket connection closed unexpectedly; reconnecting")
                await self._reconnect_rtu()
                continue
            except Exception:
                logger.exception("Unexpected callback failure")
                await asyncio.sleep(0)
                break

    @_default_timeout_arg
    async def _connect_rtu_socket(self, timeout: float):
        """Opens a websocket connection to Noteable RTU."""
        # Origin is needed, else the server request crashes and rejects the connection
        headers = {'Authorization': self.headers['authorization'], 'Origin': self.origin}
        self.rtu_socket = await websockets.connect(
            self.ws_uri, extra_headers=headers, open_timeout=timeout
        )
        logger.debug("Opened websocket connection")

    async def _resubscribe_channels(self):
        """Rehydrates the session by re-authenticating and re-subscribing to all channels."""
        await self.authenticate()
        for channel in self.subscriptions:
            # Only re-subscribe to the files channels
            if channel.startswith("files/"):
                await self.subscribe_file(channel.split('/')[1])

        # set to None so that the next connection failure will trigger a reconnect
        self.reconnect_rtu_task = None

    async def _reconnect_rtu(self):
        """Reconnects the RTU websocket connection."""
        await self._connect_rtu_socket()
        if not self.reconnect_rtu_task:
            self.reconnect_rtu_task = asyncio.create_task(self._resubscribe_channels())

    @_requires_ws_context
    @backoff.on_exception(
        backoff.expo, websockets.exceptions.ConnectionClosedError, max_time=EXP_BACKOFF_MAX_TIME
    )
    async def send_rtu_request(self, req: GenericRTURequestSchema):
        """Wraps converting a pydantic request model to be sent down the websocket."""
        logger.debug(f"Sending websocket request: {req}")
        try:
            return await self.rtu_socket.send(req.json())
        except websockets.exceptions.ConnectionClosedError:
            logger.debug(
                "Websocket connection closed unexpectedly while trying to send RTU request; reconnecting"
            )
            await self._reconnect_rtu()
            # Raise the exception to trigger backoff
            raise

    @_requires_ws_context
    @_default_timeout_arg
    async def authenticate(self, timeout: float):
        """Authenticates a fresh websocket as the given user."""

        async def authorized(resp: AuthenticationReply):
            if resp.data.success:
                logger.debug("User is authenticated!")
                self.user = resp.data.user
            else:
                raise ValueError("Failed to authenticate websocket session")
            return resp

        # Register the transaction reply after sending the request
        req = AuthenticationRequest(
            transaction_id=uuid4(), data=AuthenticationRequestData(token=self.config.token)
        )
        tracker = AuthenticationReply.register_callback(self, req, authorized)
        await self.send_rtu_request(req)
        # Give it timeout seconds to respond
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def ping_rtu(self, timeout: float):
        """Sends a ping request to the RTU websocket and confirms the response is valid."""

        async def pong(resp: GenericRTUReply):
            """The pong response for pinging a webrowser"""
            logger.debug("Initial ping response received! Websocket is live.")
            return resp  # Do nothing, we just want to ensure we reach the event

        # Register the transaction reply after sending the request
        req = PingRequest(transaction_id=uuid4())
        tracker = PingReply.register_callback(self, req, pong)
        await self.send_rtu_request(req)
        # Give it timeout seconds to respond
        pong_resp = await asyncio.wait_for(tracker.next_trigger, timeout)
        # These should be consistent, but validate for good measure
        assert pong_resp.transaction_id == req.transaction_id
        assert pong_resp.event == "ping_reply"
        assert pong_resp.channel == "system"
        return pong_resp

    def _gen_subscription_request(self, channel: str):
        async def process_subscribe(resp: GenericRTUReplySchema[TopicActionReplyData]):
            # This is needed in case other events from the same transaction are received
            # before the subscribe_reply (for e.g. update_user_file_subscription_event)
            if resp.event != "subscribe_reply":
                raise SkipCallback("This callback only processes subscribe_reply")
            resp = FileSubscribeReplySchema.parse_obj(resp)
            if resp.data.success:
                self.subscriptions.add(resp.channel)
            else:
                logger.error(f"Failed to subscribe to channel topic: {channel}")
            return resp

        # Register the reply first
        tracker = self.register_message_callback(
            process_subscribe,
            channel,
            transaction_id=uuid4(),
        )
        req = GenericRTURequest(
            transaction_id=tracker.transaction_id, event="subscribe_request", channel=channel
        )
        return req, tracker

    @_requires_ws_context
    @_default_timeout_arg
    async def subscribe_channel(self, channel: str, timeout: float):
        """A generic pattern for subscribing to topic channels."""
        req, tracker = self._gen_subscription_request(channel)
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @staticmethod
    def files_channel(file_id):
        """Helper to build file channel names from file ids"""
        return f"files/{file_id}"

    @staticmethod
    def kernels_channel(file_id: uuid.UUID):
        file_id_part = file_id.hex[:20]
        notebook_kernel_id = f"notebook-kernel-{file_id_part}"[:63]
        return f"kernels/{notebook_kernel_id}"

    @_requires_ws_context
    @_default_timeout_arg
    async def subscribe_file(
        self,
        file: Union[UUID, NotebookFile],
        timeout: float,
        from_version_id: Optional[UUID] = None,
    ):
        """Subscribes to a specified file for updates about it's contents."""
        if isinstance(file, NotebookFile):
            # TODO: Write test for file
            file_id = file.id
            # from_delta_id = file.last_save_delta_id
            from_version_id = file.current_version_id
        else:
            file_id = file
            # from_delta_id = from_delta_id
        channel = self.files_channel(file_id)
        req, tracker = self._gen_subscription_request(channel)
        # TODO: write test for these fields
        req.data = {}
        if from_version_id:
            req.data['from_version_id'] = from_version_id
        # TODO: Handle delta catchups?
        # if from_delta_id:
        #     req.data['from_delta_id'] = from_delta_id

        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def replace_cell_contents(
        self, file: NotebookFile, cell_id: str, contents: str, timeout: float
    ):
        """Sends an RTU request to replace the contents of a particular cell in a particular file."""

        async def check_success(resp: GenericRTUReplySchema[TopicActionReplyData]):
            if not resp.data.success:
                raise RTUError(f"Failed to submit cell change for file {file.id} -> {cell_id}")
            return resp

        req = file.generate_delta_request(
            uuid4(),
            FileDeltaType.cell_contents,
            FileDeltaAction.replace,
            cell_id,
            properties=V2CellContentsProperties(source=contents),
        )
        tracker = FileDeltaReply.register_callback(self, req, check_success)
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def delete_cell(self, file: NotebookFile, cell_id: str, timeout: float):
        """Sends an RTU request to delete a particular cell in a particular file."""

        async def check_success(resp: GenericRTUReplySchema[TopicActionReplyData]):
            if not resp.data.success:
                raise RTUError(f"Failed to submit cell delete for file {file.id} -> {cell_id}")
            return resp

        req = file.generate_delta_request(
            uuid4(),
            FileDeltaType.nb_cells,
            FileDeltaAction.delete,
            cell_id,
            properties=NBCellProperties(id=cell_id),
        )
        tracker = FileDeltaReply.register_callback(self, req, check_success)
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def add_cell(
        self, file: NotebookFile, cell: Dict[str, Any], after_id: str, timeout: float
    ):
        """Sends an RTU request to add a cell"""

        async def check_success(resp: GenericRTUReplySchema[TopicActionReplyData]):
            if not resp.data.success:
                raise RTUError(f"Failed to add cell for file {file.id}")
            return resp

        req = file.generate_delta_request(
            uuid4(),
            FileDeltaType.nb_cells,
            FileDeltaAction.add,
            cell['id'],
            properties=NBCellProperties(id=cell['id'], cell=cell, after_id=after_id),
        )
        tracker = self.register_message_callback(
            check_success,
            channel=self.files_channel(file.id),
            message_type="new_delta_reply",
        )
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def update_cell_metadata(
        self,
        file: NotebookFile,
        cell_id: str,
        metadata_update_properties: V2CellMetadataProperties,
        timeout: float,
    ):
        """Sends an RTU request to update the metadata of a cell"""

        async def check_success(resp: GenericRTUReplySchema[TopicActionReplyData]):
            if not resp.data.success:
                raise RTUError(f"Failed to update metadata for cell {cell_id} in file {file.id}")
            return resp

        req = file.generate_delta_request(
            uuid4(),
            FileDeltaType.cell_metadata,
            FileDeltaAction.update,
            cell_id,
            properties=metadata_update_properties,
        )
        # Explicitly register the message callback here against the message_type of new_delta_reply
        # since using FileDeltaReply.register_callback will register against the transaction_id
        # which fails because there is a `new_delta_event` message type that is sent before the
        # `new_delta_reply` message type from the same transaction_id.
        # This breaks the schema validation because the `new_delta_event` message type does not
        # have a `data.success` field.
        tracker = self.register_message_callback(
            check_success,
            channel=self.files_channel(file.id),
            message_type="new_delta_reply",
            response_schema=FileDeltaReply,
        )
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def update_nb_metadata(
        self, file: NotebookFile, metadata_update_properties: NBMetadataProperties, timeout: float
    ):
        """Sends an RTU request to update the metadata of a notebook"""

        async def check_success(resp: GenericRTUReplySchema[TopicActionReplyData]):
            if not resp.data.success:
                raise RTUError(f"Failed to update nb metadata for {file.id}")
            return resp

        req = file.generate_delta_request(
            uuid4(),
            FileDeltaType.nb_metadata,
            FileDeltaAction.update,
            properties=metadata_update_properties,
        )
        tracker = self.register_message_callback(
            check_success,
            channel=self.files_channel(file.id),
            message_type="new_delta_reply",
            response_schema=FileDeltaReply,
        )
        await self.send_rtu_request(req)
        return await asyncio.wait_for(tracker.next_trigger, timeout)

    @_requires_ws_context
    @_default_timeout_arg
    async def execute(
        self,
        file: NotebookFile,
        cell_id: str = None,
        before_id: Optional[str] = None,
        after_id: Optional[str] = None,
        await_results: bool = True,
        timeout: float = None,  # Wrapper sets the for us so the type hint is correct
    ):
        """Sends an RTU request to execute a part of the Notebook NotebookFile."""
        assert not before_id or not after_id, 'Cannot define both a before_id and after_id'
        assert not cell_id or not after_id, 'Cannot define both a cell_id and after_id'
        assert not cell_id or not before_id, 'Cannot define both a cell_id and before_id'

        action = FileDeltaAction.execute_all
        if cell_id:
            action = FileDeltaAction.execute
        elif before_id:
            action = FileDeltaAction.execute_before
            cell_id = before_id
        elif after_id:
            action = FileDeltaAction.execute_after
            cell_id = after_id

        async def check_success(resp: GenericRTUReply):
            if resp.event != 'new_delta_reply':
                raise SkipCallback("Looking for reply to request, not execution updates")
            data = resp.data or {}
            if not data.get('success', False):
                logger.error(
                    f"Failed to submit execute request for file {file.id} -> {action}({cell_id})"
                )
            return resp

        req = file.generate_delta_request(
            uuid4(), FileDeltaType.cell_execute, action, cell_id, None
        )
        tracker = GenericRTUReply.register_callback(self, req, check_success)
        tracker_future = tracker.next_trigger
        results_tracker_future = None

        async def cell_complete_check(resp: BulkCellStateMessage):
            for cell_state in resp.data.cell_states:
                if cell_state.cell_id == cell_id and cell_state.state.is_terminal_state:
                    return cell_state
                elif cell_state.cell_id == cell_id and not cell_state.state.is_terminal_state:
                    raise SkipCallback("Not terminal state")
            raise SkipCallback("Not tracked cell")

        if await_results:
            assert (
                action == FileDeltaAction.execute
            ), "Haven't implemented awaiting results for batch execution yet, sorry"
            # Register this before we start execution so we don't miss fast cells concluding
            results_tracker = self.register_message_callback(
                cell_complete_check,
                self.kernels_channel(file.id),
                "bulk_cell_state_update_event",
                response_schema=BulkCellStateMessage,
            )
            results_tracker_future = results_tracker.next_trigger

        await self.send_rtu_request(req)
        if tracker_future.done():
            execute_resp = tracker_future.result()
        else:
            execute_resp = await asyncio.wait_for(tracker_future, timeout)

        if await_results:
            if not results_tracker_future.done():
                # No timeout here because the cell could run for any given amount of time
                return await results_tracker_future
        else:
            return execute_resp
