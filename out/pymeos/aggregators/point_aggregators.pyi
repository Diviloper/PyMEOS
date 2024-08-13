from pymeos_cffi import *
from ..boxes import STBox as STBox
from ..main import TPoint as TPoint
from .aggregator import BaseAggregator as BaseAggregator

class TemporalPointExtentAggregator(BaseAggregator[TPoint, STBox]): ...
