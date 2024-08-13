from .dateset import DateSet as DateSet
from .datespan import DateSpan as DateSpan
from .datespanset import DateSpanSet as DateSpanSet
from .tstzset import TsTzSet as TsTzSet
from .tstzspan import TsTzSpan as TsTzSpan
from .tstzspanset import TsTzSpanSet as TsTzSpanSet
from datetime import date, datetime

Time = datetime | TsTzSet | TsTzSpan | TsTzSpanSet
TimeDate = date | DateSet | DateSpan | DateSpanSet
