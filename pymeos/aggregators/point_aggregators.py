from pymeos_cffi import tspatial_extent_transfn

from .aggregator import BaseAggregator
from ..boxes import STBox
from ..main import TPoint


class TemporalPointExtentAggregator(BaseAggregator[TPoint, STBox]):
    """
    Spatiotemporal extent of aggregated temporal points, i.e. smallest :class:`~pymeos.time.boxes.STBox` that
    includes all aggregated temporal numbers.

    MEOS Functions:
        tspatial_extent_transfn, temporal_tagg_finalfn
    """

    _add_function = tspatial_extent_transfn

    @classmethod
    def _finish(cls, state) -> STBox:
        return STBox(_inner=state)
