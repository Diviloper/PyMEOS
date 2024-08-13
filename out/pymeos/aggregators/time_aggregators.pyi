from ..collections import (
    TsTzSet as TsTzSet,
    TsTzSpan as TsTzSpan,
    TsTzSpanSet as TsTzSpanSet,
)
from .aggregator import BaseAggregator as BaseAggregator
from datetime import datetime

class TimeInstantaneousUnionAggregator(BaseAggregator[datetime | TsTzSet, TsTzSet]): ...
class TimeContinuousUnionAggregator(
    BaseAggregator[TsTzSpan | TsTzSpanSet, TsTzSpanSet]
): ...
