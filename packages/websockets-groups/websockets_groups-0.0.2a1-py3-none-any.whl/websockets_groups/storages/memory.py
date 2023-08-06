import asyncio
import logging
from collections import defaultdict
from typing import DefaultDict, Iterable

from websockets_groups.connects import AsyncWebSocketConnect
from websockets_groups.storages.base import BaseStorage

logger = logging.getLogger('websockets_groups')


class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        self._groups: DefaultDict[str, set[AsyncWebSocketConnect]] = defaultdict(set)
        self._messages = asyncio.Queue()

    async def register_connect(self, ws_connect: AsyncWebSocketConnect, groups: Iterable[str]) -> str:
        conn_uuid = await self._generate_uuid(ws_connect)

        logger.info(f'Регистрация подключения "{conn_uuid}" в реестре групп')

        for group in groups:
            self._groups[group].add(conn_uuid)
        return conn_uuid

    async def delete_connect(self, ws_connect: AsyncWebSocketConnect):
        conn_uuid = await self._generate_uuid(ws_connect)
        logger.info(f'Удаление подключения "{conn_uuid}" из реестра групп')

        for group in self._groups.values():
            group.discard(conn_uuid)

    async def groups(self) -> tuple[str, ...]:
        return tuple(str(i) for i in self._groups.keys())

    async def get_groups_member(self, group_name: str) -> set[AsyncWebSocketConnect]:
        return self._groups[group_name]

    async def add_message_to_queue(self, message):
        logger.info(f'Добавление сообщения в очередь: {message}')

        await self._messages.put(message)

    async def get_new_message(self):
        while True:
            message = await self._messages.get()
            yield message

    async def close(self) -> None:
        pass
