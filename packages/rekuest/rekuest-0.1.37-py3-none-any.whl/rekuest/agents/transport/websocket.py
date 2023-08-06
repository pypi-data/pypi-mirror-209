from typing import Awaitable, Callable, Dict, Any
import websockets
from rekuest.agents.transport.base import AgentTransport
import asyncio
import json
from rekuest.agents.transport.errors import (
    AgentTransportException,
    AssignationListDeniedError,
    ProvisionListDeniedError,
)
from rekuest.agents.transport.protocols.agent_json import *
import logging
from websockets.exceptions import ConnectionClosedError, InvalidStatusCode
from rekuest.api.schema import LogLevelInput
import ssl
import certifi
from koil.types import ContextBool, Contextual

logger = logging.getLogger(__name__)


async def token_loader():
    raise NotImplementedError(
        "Websocket transport does need a defined token_loader on Connection"
    )


class CorrectableConnectionFail(AgentTransportException):
    pass


class DefiniteConnectionFail(AgentTransportException):
    pass


class WebsocketAgentTransport(AgentTransport):
    endpoint_url: str
    ssl_context: ssl.SSLContext = Field(
        default_factory=lambda: ssl.create_default_context(cafile=certifi.where())
    )
    token_loader: Callable[[], Awaitable[str]] = Field(exclude=True)
    max_retries = 5
    time_between_retries = 3
    allow_reconnect = True
    auto_connect = True

    _futures: Contextual[Dict[str, asyncio.Future]] = None
    _connected: ContextBool = False
    _healthy: ContextBool = False
    _send_queue: Contextual[asyncio.Queue] = None
    _connection_task: Contextual[asyncio.Task] = None

    async def __aenter__(self):
        assert self._abroadcast is not None, "Broadcast ss be defined"
        self._futures = {}
        self._send_queue = asyncio.Queue()

    async def aconnect(self, instance_id: str):
        self._connection_task = asyncio.create_task(self.websocket_loop(instance_id))
        self._connected = True

    async def websocket_loop(self, instance_id: str, retry=0, reload_token=False):
        send_task = None
        receive_task = None
        try:
            try:
                token = await self.token_loader(force_refresh=reload_token)

                async with websockets.connect(
                    f"{self.endpoint_url}?token={token}&instance_id={instance_id}",
                    ssl=(
                        self.ssl_context
                        if self.endpoint_url.startswith("wss")
                        else None
                    ),
                ) as client:
                    logger.info("Agent on Websockets connected")

                    send_task = asyncio.create_task(self.sending(client))
                    receive_task = asyncio.create_task(self.receiving(client))

                    self._healthy = True
                    done, pending = await asyncio.wait(
                        [send_task, receive_task],
                        return_when=asyncio.FIRST_EXCEPTION,
                    )
                    self._healthy = False

                    for task in pending:
                        task.cancel()

                    for task in done:
                        raise task.exception()

            except InvalidStatusCode as e:
                logger.warning(
                    (
                        "Websocket to"
                        f" {self.endpoint_url}?token={token}&instance_id={instance_id} was"
                        " denied. Trying to reload token"
                    ),
                    exc_info=True,
                )
                reload_token = True
                raise CorrectableConnectionFail from e

            except ConnectionClosedError as e:
                logger.warning("Websocket was closed", exc_info=True)
                raise CorrectableConnectionFail from e

            except Exception as e:
                logger.warning("Websocket excepted. Trying to recover", exc_info=True)
                raise CorrectableConnectionFail from e

        except CorrectableConnectionFail as e:
            logger.info(f"Trying to Recover from Exception {e}")
            if retry > self.max_retries or not self.allow_reconnect:
                logger.error("Max retries reached. Giving up")
                raise DefiniteConnectionFail("Exceeded Number of Retries")

            await asyncio.sleep(self.time_between_retries)
            logger.info("Retrying to connect")
            await self.websocket_loop(
                instance_id, retry=retry + 1, reload_token=reload_token
            )

        except DefiniteConnectionFail as e:
            logger.error("Websocket excepted closed definetely", exc_info=True)
            self.connection_dead = False
            raise e

        except asyncio.CancelledError as e:
            logger.info("Websocket got cancelled. Trying to shutdown graceully")
            if send_task and receive_task:
                send_task.cancel()
                receive_task.cancel()

            await asyncio.gather(send_task, receive_task, return_exceptions=True)
            raise e

    async def sending(self, client):
        try:
            while True:
                message = await self._send_queue.get()
                logger.debug(f">>>> {message}")
                await client.send(message)
                self._send_queue.task_done()
        except asyncio.CancelledError:
            logger.info("Sending Task sucessfully Cancelled")

    async def receiving(self, client):
        try:
            async for message in client:
                logger.info(f"Receiving message {message}")
                await self.receive(message)
        except asyncio.CancelledError:
            logger.info("Receiving Task sucessfully Cancelled")

    async def receive(self, message):
        json_dict = json.loads(message)
        logger.debug(f"<<<< {message}")
        if "type" in json_dict:
            type = json_dict["type"]
            id = json_dict["id"]

            # State Layer
            if type == AgentSubMessageTypes.ASSIGN:
                await self._abroadcast(AssignSubMessage(**json_dict))

            if type == AgentSubMessageTypes.UNASSIGN:
                await self._abroadcast(UnassignSubMessage(**json_dict))

            if type == AgentSubMessageTypes.UNPROVIDE:
                await self._abroadcast(UnprovideSubMessage(**json_dict))

            if type == AgentSubMessageTypes.PROVIDE:
                await self._abroadcast(ProvideSubMessage(**json_dict))

            if type == AgentMessageTypes.LIST_ASSIGNATIONS_REPLY:
                self._futures[id].set_result(AssignationsListReply(**json_dict))
            if type == AgentMessageTypes.LIST_ASSIGNATIONS_DENIED:
                self._futures[id].set_exception(
                    AssignationListDeniedError(json_dict["error"])
                )

            if type == AgentMessageTypes.LIST_PROVISIONS_REPLY:
                self._futures[id].set_result(ProvisionListReply(**json_dict))
            if type == AgentMessageTypes.LIST_PROVISIONS_DENIED:
                self._futures[id].set_exception(
                    ProvisionListDeniedError(json_dict["error"])
                )

        else:
            logger.error(f"Unexpected messsage: {json_dict}")

    async def awaitaction(self, action: JSONMessage):
        assert self._connected, "Should be connected"
        if action.id in self._futures:
            raise ValueError("Action already has a future")

        future = asyncio.Future()
        self._futures[action.id] = future
        await self._send_queue.put(action.json())
        return await future

    async def delayaction(self, action: JSONMessage):
        assert self._connected, "Should be connected"
        await self._send_queue.put(action.json())

    async def list_provisions(
        self, exclude: Optional[ProvisionStatus] = None
    ) -> List[Provision]:
        action = ProvisionList(exclude=exclude)
        prov_list_reply: ProvisionListReply = await self.awaitaction(action)
        return prov_list_reply.provisions

    async def change_provision(
        self,
        id: str,
        status: ProvisionStatus = None,
        message: str = None,
        mode: ProvisionMode = None,
    ):
        action = ProvisionChangedMessage(
            provision=id, status=status, message=message, mode=mode
        )
        await self.delayaction(action)

    async def change_assignation(
        self,
        id: str,
        status: AssignationStatus = None,
        message: str = None,
        returns: List[Any] = None,
        progress: int = None,
    ):
        action = AssignationChangedMessage(
            assignation=id,
            status=status,
            message=message,
            returns=returns,
            progress=progress,
        )
        await self.delayaction(action)

    async def list_assignations(
        self, exclude: Optional[AssignationStatus] = None
    ) -> List[Assignation]:
        action = AssignationsList(exclude=exclude)
        ass_list_reply: AssignationsListReply = await self.awaitaction(action)
        return ass_list_reply.assignations

    async def log_to_assignation(
        self, id: str, level: LogLevelInput = None, message: str = None
    ):
        action = AssignationLogMessage(assignation=id, level=level, message=message)
        await self.delayaction(action)

    async def log_to_provision(
        self, id: str, level: LogLevelInput = None, message: str = None
    ):
        action = ProvisionLogMessage(provision=id, level=level, message=message)
        await self.delayaction(action)

    async def adisconnect(self):
        self._connection_task.cancel()
        self._connected = False

        try:
            await self._connection_task
        except asyncio.CancelledError:
            pass

        self._connection_task = None

    async def __aexit__(self, *args, **kwargs):
        if self._connection_task:
            await self.adisconnect()

    class Config:
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True
        copy_on_model_validation = False
