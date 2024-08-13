from datetime import timedelta
from typing import TypeVar

Self = TypeVar("Self", bound="Temporal[Any]")

class TSimplifiable:
    def simplify_min_distance(self, distance: float) -> Self: ...
    def simplify_min_tdelta(self, distance: timedelta) -> Self: ...
    def simplify_douglas_peucker(
        self, distance: float, synchronized: bool = False
    ) -> Self: ...
    def simplify_max_distance(
        self, distance: float, synchronized: bool = False
    ) -> Self: ...
