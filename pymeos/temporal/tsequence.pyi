from pymeos_cffi import *
import abc
from .interpolation import TInterpolation as TInterpolation
from .temporal import Temporal as Temporal
from _typeshed import Incomplete
from abc import ABC
from typing import Any, TypeVar

TBase = TypeVar('TBase')
TG = TypeVar('TG', bound='Temporal[Any]')
TI = TypeVar('TI', bound='TInstant[Any]')
TS = TypeVar('TS', bound='TSequence[Any]')
TSS = TypeVar('TSS', bound='TSequenceSet[Any]')
Self = TypeVar('Self', bound='TSequence[Any]')

class TSequence(Temporal[TBase, TG, TI, TS, TSS], ABC, metaclass=abc.ABCMeta):
    def __init__(self, string: str | None = None, *, instant_list: list[str | Any] | None = None, lower_inc: bool = True, upper_inc: bool = False, interpolation: TInterpolation = ..., normalize: bool = True, _inner: Incomplete | None = None) -> None: ...
    @classmethod
    def from_instants(cls, instant_list: list[str | Any] | None, lower_inc: bool = True, upper_inc: bool = False, interpolation: TInterpolation = ..., normalize: bool = True) -> Self: ...
    def lower_inc(self) -> bool: ...
    def upper_inc(self) -> bool: ...
    def plot(self, *args, **kwargs): ...
