import psycopg
from .db_objects import db_objects as db_objects
from psycopg.adapt import Buffer as Buffer, Dumper
from typing import Any

class _PymeosDumper(Dumper):
    def dump(self, obj: Any) -> Buffer: ...

class MobilityDB:
    @classmethod
    def connect(cls, *args, **kwargs): ...
    @classmethod
    def register(cls, connection: psycopg.Connection): ...
