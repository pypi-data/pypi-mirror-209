import json
from dataclasses import asdict
from typing import Any, Iterable, Optional

try:
    from redis.asyncio.client import Redis
except ImportError as ex:
    raise ImportError('Для работы RedisStorage нужно установить "redis": pip install redis') from ex

import logging

from websockets_groups.connects import AsyncWebSocketConnect
from websockets_groups.storages.base import BaseStorage

logger = logging.getLogger('websockets_groups')


class RedisStorage(BaseStorage):
    def __init__(self, redis: Redis, messages_key: str = 'channel:messages') -> None:
        self.redis = redis
        self.messages_key = messages_key
        self.psub_messages = self.redis.pubsub(ignore_subscribe_messages=True)

    @classmethod
    def from_url(
        cls,
        url: str,
        connection_kwargs: Optional[dict[str, Any]] = {},
        **kwargs: Any,
    ) -> 'RedisStorage':
        """
        Создает объект класса RedisStorage.

        Args:
            param url (str): пример redis://user:password@host:port/db
            param connection_kwargs: смотри документацию redis
            param kwargs: аргументы для передачи в  класс RedisStorage

        Returns:
            Объект класса RedisStorage
        """
        connection_kwargs.update(decode_responses=True)
        redis = Redis.from_url(url=url, **connection_kwargs)
        return cls(redis=redis, **kwargs)

    async def close(self) -> None:
        await self.redis.close()

    async def get_new_message(self):
        pubsub = self.redis.pubsub()
        await pubsub.subscribe(self.messages_key)
        while True:
            message = await pubsub.get_message(
                ignore_subscribe_messages=True,
                timeout=None,
            )
            if message:
                print(f'Receive: {message}')
                try:
                    message = json.loads(message['data'])
                    yield message
                except Exception as e:
                    # TODO неинформативное логирование
                    logger.error(f'{e}')

    async def add_message_to_queue(self, message):
        logger.info(f'Добавление сообщения в очередь: {message}')
        data = json.dumps(asdict(message))
        await self.redis.publish(self.messages_key, data)

    async def register_connect(self, ws_connect: AsyncWebSocketConnect, groups: Iterable[str]):
        conn_uuid = await self._generate_uuid(ws_connect)

        logger.info(f'Регистрация подключения "{conn_uuid}" в реестре')
        for group in groups:
            await self.redis.sadd(f'group:{group}', conn_uuid)
            await self.redis.sadd(f'{conn_uuid}:groups', f'group:{group}')
        return conn_uuid

    async def delete_connect(self, ws_connect: AsyncWebSocketConnect):
        conn_uuid = await self._generate_uuid(ws_connect)
        logger.info(f'Удаление подключения "{conn_uuid}" из реестра')
        connect_groups = await self.redis.smembers(f'{conn_uuid}:groups')
        for groups in connect_groups:
            await self.redis.srem(groups, conn_uuid)

    async def groups(self) -> tuple[str, ...]:
        return await self.redis.keys('group:*')

    async def get_groups_member(self, group_name: str) -> set[AsyncWebSocketConnect]:
        return await self.redis.smembers(f'group:{group_name}')
