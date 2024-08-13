from ..base import Span as Span
from .floatset import FloatSet as FloatSet
from .floatspanset import FloatSpanSet as FloatSpanSet
from .intspan import IntSpan as IntSpan
from typing import overload

class FloatSpan(Span[float]):
    def to_spanset(self) -> FloatSpanSet: ...
    def to_intspan(self) -> IntSpan: ...
    def lower(self) -> float: ...
    def upper(self) -> float: ...
    def width(self) -> float: ...
    def shift(self, delta: float) -> FloatSpan: ...
    def scale(self, width: float) -> FloatSpan: ...
    def shift_scale(self, delta: float | None, width: float | None) -> FloatSpan: ...
    def is_adjacent(self, other: int | float | FloatSpan | FloatSpanSet) -> bool: ...
    def contains(self, content: int | float | FloatSpan | FloatSpanSet) -> bool: ...
    def is_same(self, other: int | float | FloatSpan | FloatSpanSet) -> bool: ...
    def is_left(self, other: int | float | FloatSpan | FloatSpanSet) -> bool: ...
    def is_over_or_left(
        self, other: int | float | FloatSpan | FloatSpanSet
    ) -> bool: ...
    def is_right(self, other: int | float | FloatSpan | FloatSpanSet) -> bool: ...
    def is_over_or_right(self, other: float | FloatSpan | FloatSpanSet) -> bool: ...
    def distance(
        self, other: int | float | FloatSet | FloatSpan | FloatSpanSet
    ) -> float: ...
    @overload
    def intersection(self, other: int | float) -> float | None: ...
    @overload
    def intersection(self, other: FloatSpan) -> FloatSpan | None: ...
    @overload
    def intersection(self, other: FloatSpanSet) -> FloatSpanSet | None: ...
    def minus(self, other: int | float | FloatSpan | FloatSpanSet) -> FloatSpanSet: ...
    def union(self, other: int | float | FloatSpan | FloatSpanSet) -> FloatSpanSet: ...
