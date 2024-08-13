import abc
from ..base.collection import Collection as Collection
from abc import ABC
from datetime import date
from typing import TypeVar

TimeClass = TypeVar("TimeClass", bound=date)

class TimeCollection(Collection[TimeClass], ABC, metaclass=abc.ABCMeta):
    def is_before(self, other) -> bool: ...
    def is_over_or_before(self, other) -> bool: ...
    def is_over_or_after(self, other) -> bool: ...
    def is_after(self, other) -> bool: ...
