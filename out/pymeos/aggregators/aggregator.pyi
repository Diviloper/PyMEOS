from pymeos_cffi import *
import abc
from ..boxes import Box as Box
from ..collections import Time as Time
from ..temporal import Temporal as Temporal
from typing import Callable, Generic, TypeVar

ResultType = TypeVar("ResultType", bound=Temporal | Time | Box)
SourceType = TypeVar("SourceType", bound=Temporal | Time | Box)
StateType = TypeVar("StateType")
SourceMeosType = TypeVar("SourceMeosType")
ResultMeosType = TypeVar("ResultMeosType")
SelfAgg = TypeVar("SelfAgg", bound="Aggregation")
IntervalType = TypeVar("IntervalType")
OriginType = TypeVar("OriginType")

class BaseAggregator(abc.ABC, Generic[SourceType, ResultType]):
    @classmethod
    def aggregate(cls, temporals: list[SourceType]) -> ResultType: ...
    @classmethod
    def start_aggregation(cls) -> Aggregation: ...

class Aggregation(Generic[SourceType, ResultType]):
    def __init__(self, add_function, finish_function) -> None: ...
    def add(self, new_temporal: SourceType) -> SelfAgg: ...
    def aggregation(self) -> ResultType: ...

class BaseGranularAggregator(Generic[SourceType, ResultType, IntervalType, OriginType]):
    @classmethod
    def aggregate(
        cls, temporals: list[SourceType], interval: IntervalType, origin: OriginType
    ) -> ResultType: ...
    @classmethod
    def start_aggregation(
        cls, interval: IntervalType, origin: OriginType
    ) -> GranularAggregation[SourceType, ResultType, IntervalType, OriginType]: ...

class GranularAggregation(
    Aggregation[SourceType, ResultType],
    Generic[SourceType, ResultType, IntervalType, OriginType],
):
    def __init__(
        self,
        add_function: Callable[
            [StateType | None, SourceType, IntervalType, OriginType], StateType
        ],
        finish_function: Callable[[StateType], ResultType],
        interval: IntervalType,
        origin: OriginType,
    ) -> None: ...
    def add(self, new_temporal: SourceType) -> SelfAgg: ...
