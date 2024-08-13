from pymeos_cffi import *
import abc
import pandas as pd
from .temporal import Temporal as Temporal, import_pandas as import_pandas
from _typeshed import Incomplete
from abc import ABC
from typing import Any, TypeVar

TBase = TypeVar('TBase')
TG = TypeVar('TG', bound='Temporal[Any]')
TI = TypeVar('TI', bound='TInstant[Any]')
TS = TypeVar('TS', bound='TSequence[Any]')
TSS = TypeVar('TSS', bound='TSequenceSet[Any]')
Self = TypeVar('Self', bound='TSequenceSet[Any]')

class TSequenceSet(Temporal[TBase, TG, TI, TS, TSS], ABC, metaclass=abc.ABCMeta):
    def __init__(self, string: str | None = None, *, sequence_list: list[str | Any] | None = None, normalize: bool = True, _inner: Incomplete | None = None) -> None: ...
    @classmethod
    def from_sequences(cls, sequence_list: list[str | Any] | None = None, normalize: bool = True) -> Self: ...
    def num_sequences(self) -> int: ...
    def start_sequence(self) -> TS: ...
    def end_sequence(self) -> TS: ...
    def sequence_n(self, n) -> TS: ...
    def sequences(self) -> list[TS]: ...
    def to_dataframe(self) -> pd.DataFrame: ...
    def plot(self, *args, **kwargs): ...
