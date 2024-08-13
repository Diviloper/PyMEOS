import asyncpg
from .db_objects import db_objects as db_objects

class MobilityDB:
    @classmethod
    async def connect(cls, *args, **kwargs) -> asyncpg.connection.Connection: ...
    @classmethod
    async def register(cls, connection: asyncpg.connection.Connection) -> None: ...
