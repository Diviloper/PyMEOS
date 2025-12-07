from datetime import datetime
from typing import TypeAlias

from ...collections import Time
from .tgeography import TGeography


class TGeographicPoint(TGeography):
    @staticmethod
    def from_base_time(value, base: Time):
        pass

    @classmethod
    def from_mfjson(cls, mfjson: str):
        pass

    def as_wkt(self) -> str:
        pass

    def value_set(self):
        pass

    def start_value(self):
        pass

    def end_value(self):
        pass

    def value_at_timestamp(self, timestamp: datetime):
        pass


TGeogPoint: TypeAlias = TGeographicPoint
