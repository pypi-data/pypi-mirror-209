# WebSockets Groups

Модуль реализующих менеджер групп WebSocket подключений

Функционал:

- Регистрация / Удаление WS
- Создание / Удаление групп WS
- Подключение WS в группу
- Поддержка реестров: memory, redis

## Quick start

Установка:

```sh
pip install websockets-groups
```

Подключение:

```python
from fastapi import WebSocket
from websockets_groups import WSGroupsManager, MemoryStorage, BaseDispatcher

ws_groups_manager = WSGroupsManager(MemoryStorage())

class ChatDispatcher(BaseDispatcher):
    pass

@app.websocket('/chats/')
async def ws_view(webdocket: WebSocket, chat_name: str):
    await ws_groups_manager.register_ws(websocket, ChatDispatcher())
```
