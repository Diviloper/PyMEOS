import psycopg2
from .db_objects import db_objects as db_objects

class MobilityDB:
    @classmethod
    def connect(cls, *args, **kwargs) -> psycopg2.extensions.connection: ...
    @classmethod
    def register(cls, connection: psycopg2.extensions.connection) -> None: ...
