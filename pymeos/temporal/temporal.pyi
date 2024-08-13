from pymeos_cffi import *
from ..collections import *
import abc
import pandas as pd
from ..boxes import Box as Box
from ..mixins import TComparable as TComparable, TTemporallyEquatable as TTemporallyEquatable
from .interpolation import TInterpolation as TInterpolation
from .tinstant import TInstant as TInstant
from .tsequence import TSequence as TSequence
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

def import_pandas(): ...
TBase = TypeVar('TBase')
TG = TypeVar('TG', bound='Temporal[Any]')
TI = TypeVar('TI', bound='TInstant[Any]')
TS = TypeVar('TS', bound='TSequence[Any]')
TSS = TypeVar('TSS', bound='TSequenceSet[Any]')
Self = TypeVar('Self', bound='Temporal[Any]')

class Temporal(TComparable, TTemporallyEquatable, ABC, Generic[TBase, TG, TI, TS, TSS], metaclass=abc.ABCMeta):
    BaseClass: Incomplete
    ComponentClass: Incomplete
    def __copy__(self) -> Self: ...
    @staticmethod
    @abstractmethod
    def from_base_time(value: TBase, base: Time) -> TG: ...
    @classmethod
    @abstractmethod
    def from_mfjson(cls, mfjson: str) -> Self: ...
    @classmethod
    def from_wkb(cls, wkb: bytes) -> Self: ...
    @classmethod
    def from_hexwkb(cls, hexwkb: str) -> Self: ...
    @classmethod
    def from_merge(cls, *temporals: TG) -> Self: ...
    @classmethod
    def from_merge_array(cls, temporals: list[TG]) -> Self: ...
    @abstractmethod
    def as_wkt(self) -> str: ...
    def as_mfjson(self, with_bbox: bool = True, flags: int = 3, precision: int = 6, srs: str | None = None) -> str: ...
    def as_wkb(self) -> bytes: ...
    def as_hexwkb(self) -> str: ...
    def bounding_box(self) -> TsTzSpan | Box: ...
    def interpolation(self) -> TInterpolation: ...
    @abstractmethod
    def value_set(self) -> set[TBase]: ...
    def values(self) -> list[TBase]: ...
    @abstractmethod
    def start_value(self) -> TBase: ...
    @abstractmethod
    def end_value(self) -> TBase: ...
    def min_value(self) -> TBase: ...
    def max_value(self) -> TBase: ...
    @abstractmethod
    def value_at_timestamp(self, timestamp: datetime) -> TBase: ...
    def time(self) -> TsTzSpanSet: ...
    def duration(self, ignore_gaps: bool = False) -> timedelta: ...
    def tstzspan(self) -> TsTzSpan: ...
    def timespan(self) -> TsTzSpan: ...
    def num_instants(self) -> int: ...
    def start_instant(self) -> TI: ...
    def end_instant(self) -> TI: ...
    def min_instant(self) -> TI: ...
    def max_instant(self) -> TI: ...
    def instant_n(self, n: int) -> TI: ...
    def instants(self) -> list[TI]: ...
    def num_timestamps(self) -> int: ...
    def start_timestamp(self) -> datetime: ...
    def end_timestamp(self) -> datetime: ...
    def timestamp_n(self, n: int) -> datetime: ...
    def timestamps(self) -> list[datetime]: ...
    def segments(self) -> list[TS]: ...
    def __hash__(self) -> int: ...
    def set_interpolation(self, interpolation: TInterpolation) -> Self: ...
    def shift_time(self, delta: timedelta) -> Self: ...
    def scale_time(self, duration: timedelta) -> Self: ...
    def shift_scale_time(self, shift: timedelta | None = None, duration: timedelta | None = None) -> Self: ...
    def temporal_sample(self, duration: str | timedelta, start: str | datetime | None = None, interpolation: TInterpolation | None = None) -> TG: ...
    def temporal_precision(self, duration: str | timedelta, start: str | datetime | None = None) -> TG: ...
    def to_instant(self) -> TI: ...
    def to_sequence(self, interpolation: TInterpolation) -> TS: ...
    def to_sequenceset(self, interpolation: TInterpolation) -> TSS: ...
    def to_dataframe(self) -> pd.DataFrame: ...
    def append_instant(self, instant: TInstant[TBase], max_dist: float | None = 0.0, max_time: timedelta | None = None) -> TG: ...
    def append_sequence(self, sequence: TSequence[TBase]) -> TG: ...
    def merge(self, other: None | Temporal[TBase] | list[Temporal[TBase]]) -> TG: ...
    def insert(self, other: TG, connect: bool = True) -> TG: ...
    def update(self, other: TG, connect: bool = True) -> TG: ...
    def delete(self, other: Time, connect: bool = True) -> TG: ...
    def at(self, other: Time) -> TG: ...
    def at_min(self) -> TG: ...
    def at_max(self) -> TG: ...
    def minus(self, other: Time) -> TG: ...
    def minus_min(self) -> TG: ...
    def minus_max(self) -> TG: ...
    def is_adjacent(self, other: Time | Temporal | Box) -> bool: ...
    def is_temporally_adjacent(self, other: Time | Temporal | Box) -> bool: ...
    def is_contained_in(self, container: Time | Temporal | Box) -> bool: ...
    def is_temporally_contained_in(self, container: Time | Temporal | Box) -> bool: ...
    def contains(self, content: Time | Temporal | Box) -> bool: ...
    def __contains__(self, item) -> bool: ...
    def temporally_contains(self, content: Time | Temporal | Box) -> bool: ...
    def overlaps(self, other: Time | Temporal | Box) -> bool: ...
    def temporally_overlaps(self, other: Time | Temporal | Box) -> bool: ...
    def is_same(self, other: Time | Temporal | Box) -> bool: ...
    def is_before(self, other: Time | Temporal | Box) -> bool: ...
    def is_over_or_before(self, other: Time | Temporal | Box) -> bool: ...
    def is_after(self, other: Time | Temporal | Box) -> bool: ...
    def is_over_or_after(self, other: Time | Temporal | Box) -> bool: ...
    def frechet_distance(self, other: Temporal) -> float: ...
    def dyntimewarp_distance(self, other: Temporal) -> float: ...
    def hausdorff_distance(self, other: Temporal) -> float: ...
    def time_split(self, duration: str | timedelta, start: str | datetime | None = None) -> list[TG]: ...
    def time_split_n(self, n: int) -> list[TG]: ...
    def stops(self, max_distance: float | None = 0.0, min_duration: timedelta | None = ...) -> TSS: ...
