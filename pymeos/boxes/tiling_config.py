from dataclasses import dataclass
from datetime import timedelta, datetime
from math import ceil
from typing import Union, TYPE_CHECKING

from pymeos_cffi import (
    pg_timestamptz_in,
    pg_interval_in,
    timedelta_to_interval,
    datetime_to_timestamptz,
)

if TYPE_CHECKING:
    from pymeos import TBox


@dataclass
class TilingConfig:
    size: Union[float, int, None] = None
    """
    Size of the numeric dimension of the tiles.
    If both ``size`` and ``numeric_tiles`` are set, ``size`` will take precedence.
    """

    numeric_tiles: Union[int, None] = None
    """
    Number of tiles in the numeric division.
    Given a ``TBox``, the tile size will be ``(box.xmax() - box.xmin()) / numeric_tiles``
    If both ``size`` and ``numeric_tiles`` are set, ``size`` will take precedence. 
    """

    duration: Union[timedelta, str] = None
    """
    Size of the temporal dimension of the tiles.
    If both ``duration`` and ``temporal_tiles`` are set, ``size`` will take precedence.
    """

    temporal_tiles: Union[int, None] = None
    """
    Number of tiles in the numeric division.
    Given a ``TBox``, the tile duration will be ``(box.tmax()-box.tmin())/temporal_tiles``
    If both ``duration`` and ``temporal_tiles`` are set, ``size`` will take precedence.
    """

    origin: Union[float, int, None] = None
    """
    Origin of the numeric dimension of the tiles.
    By default, the start of the TBox (``box.xmin()``)
    """

    start: Union[datetime, str, None] = None
    """
    Origin of the temporal dimension of the tiles. 
    By default, the start of the TBox (``box.tmin()``)
    """

    def get_size(self, box: TBox) -> Union[int, float]:
        if self.size is None and self.numeric_tiles is None:
            size = (box.xmax() - box.xmin()) + 1
        elif self.size is not None:
            size = self.size
        else:
            size = (box.xmax() - box.xmin()) / self.numeric_tiles

        if box._is_float():
            return float(size)
        else:
            return int(ceil(size))

    def get_duration(self, box: TBox) -> "Interval":
        if self.duration is not None:
            if isinstance(self.duration, str):
                return pg_interval_in(self.duration, -1)
            if isinstance(self.duration, timedelta):
                return timedelta_to_interval(self.duration)
            raise ValueError(
                f"Invalid duration. Expected a string or a timedelta. "
                f"Got {self.duration} ({type(self.duration)})"
            )
        elif self.temporal_tiles is not None:
            duration = box.tmax() - box.tmin()
            return timedelta_to_interval(duration / self.temporal_tiles)
        else:
            duration = box.tmax() - box.tmin()
            return timedelta_to_interval(duration)

    def get_origin(self, box: TBox) -> Union[int, float]:
        if self.origin is None:
            return box.xmin()
        if box._is_float():
            return float(self.origin)
        else:
            return int(ceil(self.origin))

    def get_start(self, box: TBox) -> "TimestampTz":
        if isinstance(self.start, str):
            return pg_timestamptz_in(self.start, -1)
        if isinstance(self.start, datetime):
            return datetime_to_timestamptz(self.start)
        return datetime_to_timestamptz(box.tmin())
