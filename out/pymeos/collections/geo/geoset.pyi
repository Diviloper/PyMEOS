import shapely as shp
from ..base import Set as Set
from abc import ABC
from typing import TypeVar, overload

Self = TypeVar("Self", bound="GeoSet")

class GeoSet(Set[shp.Geometry], ABC):
    def as_ewkt(self, max_decimals: int = 15) -> str: ...
    def as_wkt(self, max_decimals: int = 15): ...
    def as_text(self, max_decimals: int = 15): ...
    def to_spanset(self) -> None: ...
    def to_span(self) -> None: ...
    def start_element(self) -> shp.Geometry: ...
    def end_element(self) -> shp.Geometry: ...
    def element_n(self, n: int) -> shp.Geometry: ...
    def elements(self) -> list[shp.Geometry]: ...
    def srid(self) -> int: ...
    def contains(self, content: GeoSet | str) -> bool: ...
    @overload
    def intersection(self, other: shp.Geometry) -> shp.Geometry | None: ...
    @overload
    def intersection(self, other: GeoSet) -> GeoSet | None: ...
    def minus(self, other: GeoSet | shp.Geometry) -> GeoSet | None: ...
    def subtract_from(self, other: shp.Geometry) -> shp.Geometry | None: ...
    def union(self, other: GeoSet | shp.Geometry) -> GeoSet: ...
    def round(self, max_decimals: int) -> Self: ...

class GeometrySet(GeoSet): ...
class GeographySet(GeoSet): ...
