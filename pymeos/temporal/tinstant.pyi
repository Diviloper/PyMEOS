from pymeos_cffi import *
import abc
from .temporal import Temporal as Temporal
from _typeshed import Incomplete
from abc import ABC
from datetime import datetime
from typing import TypeVar

TBase = TypeVar('TBase')
TG = TypeVar('TG', bound='Temporal[Any]')
TI = TypeVar('TI', bound='TInstant[Any]')
TS = TypeVar('TS', bound='TSequence[Any]')
TSS = TypeVar('TSS', bound='TSequenceSet[Any]')
Self = TypeVar('Self', bound='TInstant[Any]')

class TInstant(Temporal[TBase, TG, TI, TS, TSS], ABC, metaclass=abc.ABCMeta):
    def __init__(self, string: str | None = None, *, value: str | TBase | None = None, timestamp: str | datetime | None = None, _inner: Incomplete | None = None) -> None: ...
    def value(self) -> TBase: ...
    def timestamp(self) -> datetime: ...
    def start_instant(self) -> Self: ...
    def end_instant(self) -> Self: ...
    def instant_n(self, n: int) -> Self: ...
    def instants(self) -> list[Self]: ...
    def start_timestamp(self) -> datetime: ...
    def end_timestamp(self) -> datetime: ...
    def timestamp_n(self, n) -> datetime: ...
    def timestamps(self) -> list[datetime]: ...
