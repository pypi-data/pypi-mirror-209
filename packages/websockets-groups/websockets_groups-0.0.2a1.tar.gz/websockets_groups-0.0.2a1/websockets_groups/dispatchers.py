from __future__ import annotations

import logging
import typing
from abc import ABC

from websockets_groups.connects import AsyncWebSocketConnect

if typing.TYPE_CHECKING:
    from websockets_groups.managers import WSGroupsManager


logger = logging.getLogger('websockets_groups')


class BaseDispatcher(ABC):
    def set_ws_connect(self, ws_connect: AsyncWebSocketConnect):
        self.ws_connect = ws_connect

    def set_manager(self, group_manager: WSGroupsManager):
        self.group_manager = group_manager

    # State

    async def before_connect(self):
        logger.debug('before_connect')

    async def on_connect(self):
        logger.debug('on_connect')

    async def before_disconnect(self):
        logger.debug('before_disconnect')

    async def on_disconnect(self):
        logger.debug('on_disconnect')

    # Processing

    async def on_message(self, message: str):
        logger.debug('from connection received message: len()={message}')

    async def on_message_from_group_queue(self, group_name: str, message: str):
        logger.debug(f'from some group "{group_name}" received message: len()={message}')
