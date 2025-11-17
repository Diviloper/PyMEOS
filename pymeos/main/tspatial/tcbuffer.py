from datetime import datetime
from typing import TypeAlias

from ...collections import Time
from .tspatial import TSpatial


class TCircularBuffer(TSpatial):
    @staticmethod
    def from_base_time(value, base: Time):
        # TODO: Implement
        pass

    @classmethod
    def from_mfjson(cls, mfjson: str):
        # TODO: Implement
        pass

    def as_wkt(self) -> str:
        # TODO: Implement
        pass

    def value_set(self):
        # TODO: Implement
        pass

    def start_value(self):
        # TODO: Implement
        pass

    def end_value(self):
        # TODO: Implement
        pass

    def value_at_timestamp(self, timestamp: datetime):
        # TODO: Implement
        pass


TCBuffer: TypeAlias = TCircularBuffer
