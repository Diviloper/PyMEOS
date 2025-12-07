from abc import ABC

from pymeos_cffi import tspatial_as_ewkt, tspatial_as_text, tspatial_to_stbox

from ...boxes import STBox
from ...temporal import Temporal


class TSpatial(Temporal, ABC):
    # ------------------------- Output ----------------------------------------

    def as_text(self, max_decimals: int = 15) -> str:
        return tspatial_as_text(self._inner, max_decimals)

    def as_wkt(self, max_decimals: int = 15) -> str:
        return tspatial_as_text(self._inner, max_decimals)

    def as_ewkt(self, max_decimals: int = 15) -> str:
        return tspatial_as_ewkt(self._inner, max_decimals)

    def bounding_box(self) -> STBox:
        """
        Returns the bounding box of `self`.
        """
        return STBox(_inner=tspatial_to_stbox(self._inner))
