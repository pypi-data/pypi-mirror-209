# from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from hashlib import md5
from uuid import UUID

from websockets_groups.connects import AsyncWebSocketConnect

logger = logging.getLogger('websockets_groups')


class BaseStorage(ABC):
    async def _generate_uuid(self, ws_connect: AsyncWebSocketConnect) -> str:
        assert ws_connect.ws.client is not None

        name = f'{id(ws_connect)}-{ws_connect.ws.client.host}:{ws_connect.ws.client.port}'
        # name = f'{id(ws)}'

        digest = md5(bytes(name, 'utf-8'), usedforsecurity=False).digest()

        return str(UUID(bytes=digest[:16], version=5))

    @abstractmethod
    async def register_connect(self, ws_connect: AsyncWebSocketConnect, groups: list[str]) -> str:
        """Добавляет коннект в множество коннектов групп и возвращает UUID коннекта"""
        pass

    @abstractmethod
    async def delete_connect(self, ws_connect: AsyncWebSocketConnect):
        pass

    @abstractmethod
    async def groups(self) -> tuple[str, ...]:
        """Получение списка групп"""
        pass

    @abstractmethod
    async def get_groups_member(self, group_name: str):
        """Возвращает пользователей группы"""
        pass

    @abstractmethod
    async def add_message_to_queue(self, message):
        """Добавление сообщения в очередь"""
        pass

    @abstractmethod
    async def get_new_message(self):
        """Вернет сообщение при наличии, иначе ждёт появления сообщения"""
        pass

    @abstractmethod
    async def close(self):
        """
        Закрывает подключение к storage
        """
        pass
