from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Iterable

from fastapi import WebSocket

from websockets_groups.connects import AsyncWebSocketConnect
from websockets_groups.dispatchers import BaseDispatcher
from websockets_groups.storages.base import BaseStorage

logger = logging.getLogger('websockets_groups')


@dataclass(frozen=True)
class Message:
    group_name: str
    text: str
    from_ws_uuid: AsyncWebSocketConnect


class WSGroupsManager:

    WS_CONNECT_CLASS: type[AsyncWebSocketConnect] = AsyncWebSocketConnect

    def __init__(self, storage: BaseStorage) -> None:
        self.storage = storage
        self._message_worker = None
        self.ws_connects: dict[str, AsyncWebSocketConnect] = {}

    async def _queue_processor(self):
        logger.info('Старт воркера чтения очереди сообщений')
        while True:
            async for message in self.storage.get_new_message():
                if not isinstance(message, Message):
                    message = Message(**message)
                logger.info(f'Отправка сообщения:{message} > в группу:{message.group_name}')
                asyncio.create_task(self._send_message_to_group(message))

    async def _send_message_to_group(self, message: Message):
        ws_uuid_list = await self.storage.get_groups_member(message.group_name)
        tasks = []
        for ws_uuid in ws_uuid_list:
            ws = self.ws_connects.get(ws_uuid)
            if ws and message.from_ws_uuid != ws_uuid:
                tasks.append(asyncio.create_task(ws.send(message.text)))
        await asyncio.gather(*tasks)

    async def groups(self) -> tuple[str, ...]:
        """Получение списка существующих групп

        Returns:
            tuple[str]: Список имен групп

        """

        return await self.storage.groups()

    async def group_send(self, group_name: str, text: str, ws):
        """Добавление сообщения в очередь на отправку"""
        ws_uuid = await self.storage._generate_uuid(ws)
        message = Message(group_name=group_name, text=text, from_ws_uuid=ws_uuid)
        return await self.storage.add_message_to_queue(message)

    async def register_ws(self, ws: WebSocket, dispatcher: BaseDispatcher, groups: Iterable[str]):
        """Регистрация и запуск WS

        Args:
            ws (WebSocket): Target WebSocket
            dispatcher (BaseDispatcher): BaseDispatcher for processing
            groups (Iterable[str]): List of group names where WebSocket will be added

        """

        assert isinstance(ws, WebSocket), 'Поддерживается только WS от starlette (FastAPI)'
        # Запускаем в фоне задачу прослушивания очереди сообщений
        if not self._message_worker:
            self._message_worker = asyncio.create_task(self._queue_processor())
        # Обертка над WebSocket
        ws_connect = self.WS_CONNECT_CLASS(ws, dispatcher)

        # Доступ к хранилищу
        dispatcher.set_manager(self)

        # Регистрация подключения в реестре
        conn_uuid = await self.storage.register_connect(ws_connect, groups)
        # добавляем коннект в список коннектов
        self.ws_connects[conn_uuid] = ws_connect

        await ws_connect.run()

        # Удаление подключения из реестре
        await self.storage.delete_connect(ws_connect)

        # удаляем коннект из списка коннектов
        del self.ws_connects[conn_uuid]
