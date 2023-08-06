from __future__ import annotations

import asyncio
import logging
import traceback
import typing

from starlette.websockets import WebSocket, WebSocketDisconnect, WebSocketState

if typing.TYPE_CHECKING:
    from websockets_groups.dispatchers import BaseDispatcher
    from websockets_groups.storages.base import BaseStorage


logger = logging.getLogger('websockets_groups')


class AsyncWebSocketConnect(object):
    dispatcher: BaseDispatcher
    ws: WebSocket
    storage: BaseStorage

    is_running: bool

    def __init__(self, ws: WebSocket, dispatcher: BaseDispatcher):
        assert ws.client is not None

        logger.debug(
            'Init connect "{}" for ws client "{}:{}" with dispatcher "{}"'.format(
                self.__class__.__name__, ws.client.host, ws.client.port, dispatcher
            )
        )

        self.ws = ws
        # self.storage = storage

        self.dispatcher = dispatcher
        self.dispatcher.set_ws_connect(self)

        self.is_running = True

    async def connect(self):
        logger.debug('WebSocket connecting')

        await self.dispatcher.before_connect()
        await self.ws.accept()
        await self.dispatcher.on_connect()

        logger.debug('WebSocket connected')

    async def disconnect(self):
        logger.debug('WebSocket disconnecting')

        self.is_running = False

        await self.dispatcher.before_disconnect()

        if self.ws.client_state != WebSocketState.DISCONNECTED:
            await self.ws.close()

        await self.dispatcher.on_disconnect()

        logger.debug('WebSocket disconnected')

    async def send(self, message: str):
        logger.debug(f'Send Message: len()={len(message)}')

        await self.ws.send_text(message)

        logger.debug('Message sent')

    async def ws_recv_message(self) -> str | None:
        logger.debug('Receive Message')

        message = await self.ws.receive_text()

        logger.debug(f'Message received: len()={len(message)}')

        return message

    async def ws_recv_loop(self):
        logger.debug('Start receive loop')
        while True:
            logger.debug('Receive loop iter')
            try:
                message = await self.ws_recv_message()
            except WebSocketDisconnect:
                break
            await self.dispatcher.on_message(message)

        logger.debug('Receive loop ended')

    async def wait_disconnect(self):
        logger.debug('wait_disconnect')
        logger.debug('wait_disconnected')

    async def run(self):
        logger.debug('WS Connect running')

        await self.connect()

        # ждем завершения recv таски
        await self.ws_recv_loop()

        await self.wait_disconnect()

        self.is_running = False

        await self.stop_tasks()
        await self.disconnect()

        logger.debug('WS Connect finished')

    async def stop_tasks(self):
        logger.error('Stop: Receive task')

        try:
            await asyncio.wait_for(self._recv_tasks, 10)

        except BaseException:
            traceback.print_exc()
