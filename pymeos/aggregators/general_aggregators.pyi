from ..boxes import Box as Box
from ..collections import Time as Time, TsTzSet as TsTzSet, TsTzSpan as TsTzSpan, TsTzSpanSet as TsTzSpanSet
from ..main import TIntSeq as TIntSeq, TIntSeqSet as TIntSeqSet
from ..temporal import TInterpolation as TInterpolation, Temporal as Temporal
from .aggregator import BaseAggregator as BaseAggregator
from datetime import datetime

class TemporalInstantCountAggregator(BaseAggregator[datetime | TsTzSet | Temporal, TIntSeq]): ...
class TemporalPeriodCountAggregator(BaseAggregator[TsTzSpan | TsTzSpanSet | Temporal, TIntSeqSet]): ...
class TemporalExtentAggregator(BaseAggregator[Time | Temporal, TsTzSpan]): ...
