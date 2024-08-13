from pymeos_cffi import *
from ..collections import *
import abc
import shapely.geometry as shp
import shapely.geometry.base as shpb
from ..boxes import Box as Box, STBox as STBox
from ..mixins import TSimplifiable as TSimplifiable
from ..temporal import (
    TInstant as TInstant,
    TInterpolation as TInterpolation,
    TSequence as TSequence,
    TSequenceSet as TSequenceSet,
    Temporal as Temporal,
)
from .tbool import TBool as TBool
from .tfloat import (
    TFloat as TFloat,
    TFloatInst as TFloatInst,
    TFloatSeq as TFloatSeq,
    TFloatSeqSet as TFloatSeqSet,
)
from _typeshed import Incomplete
from abc import ABC
from geopandas import GeoDataFrame as GeoDataFrame
from typing import TypeVar, overload

def import_geopandas(): ...

TG = TypeVar("TG", bound="TPoint")
TI = TypeVar("TI", bound="TPointInst")
TS = TypeVar("TS", bound="TPointSeq")
TSS = TypeVar("TSS", bound="TPointSeqSet")
Self = TypeVar("Self", bound="TPoint")
TF = TypeVar("TF", bound="TFloat", covariant=True)

class TPoint(
    Temporal[shp.Point, TG, TI, TS, TSS], TSimplifiable, ABC, metaclass=abc.ABCMeta
):
    def __init__(self, _inner) -> None: ...
    @classmethod
    def from_hexwkb(cls, hexwkb: str, srid: int | None = None) -> Self: ...
    def as_wkt(self, precision: int = 15) -> str: ...
    def as_ewkt(self, precision: int = 15) -> str: ...
    def as_geojson(
        self, option: int = 1, precision: int = 15, srs: str | None = None
    ) -> str: ...
    def to_shapely_geometry(self, precision: int = 15) -> shpb.BaseGeometry: ...
    def bounding_box(self) -> STBox: ...
    def values(self, precision: int = 15) -> list[shp.Point]: ...
    def start_value(self, precision: int = 15) -> shp.Point: ...
    def end_value(self, precision: int = 15) -> shp.Point: ...
    def value_set(self, precision: int = 15) -> set[shp.Point]: ...
    def value_at_timestamp(
        self, timestamp: datetime, precision: int = 15
    ) -> shp.Point: ...
    def length(self) -> float: ...
    def cumulative_length(self) -> TFloat: ...
    def speed(self) -> TFloat: ...
    def x(self) -> TF: ...
    def y(self) -> TF: ...
    def z(self) -> TF: ...
    def has_z(self) -> bool: ...
    def stboxes(self) -> list[STBox]: ...
    def is_simple(self) -> bool: ...
    def bearing(self, other: shpb.BaseGeometry | TPoint) -> TFloat: ...
    def direction(self) -> float: ...
    def azimuth(self) -> TFloatSeqSet: ...
    def angular_difference(self) -> TFloatSeqSet: ...
    def time_weighted_centroid(self, precision: int = 15) -> shp.Point: ...
    def srid(self) -> int: ...
    def set_srid(self, srid: int) -> Self: ...
    def round(self, max_decimals: int = 0) -> TPoint: ...
    def make_simple(self) -> list[TPoint]: ...
    def expand(self, other: int | float) -> STBox: ...
    def transform(self, srid: int) -> Self: ...
    def at(self, other: shpb.BaseGeometry | GeoSet | STBox | Time) -> TG: ...
    def minus(self, other: shpb.BaseGeometry | GeoSet | STBox | Time) -> TG: ...
    def is_left(self, other: Temporal | Box) -> bool: ...
    def is_over_or_left(self, other: Temporal | Box) -> bool: ...
    def is_right(self, other: Temporal | Box) -> bool: ...
    def is_over_or_right(self, other: Temporal | Box) -> bool: ...
    def is_below(self, other: Temporal | Box) -> bool: ...
    def is_over_or_below(self, other: Temporal | Box) -> bool: ...
    def is_above(self, other: Temporal | Box) -> bool: ...
    def is_over_or_above(self, other: Temporal | Box) -> bool: ...
    def is_front(self, other: Temporal | Box) -> bool: ...
    def is_over_or_front(self, other: Temporal | Box) -> bool: ...
    def is_behind(self, other: Temporal | Box) -> bool: ...
    def is_over_or_behind(self, other: Temporal | Box) -> bool: ...
    def is_ever_contained_in(self, container: shpb.BaseGeometry | STBox) -> bool: ...
    def is_ever_disjoint(self, other: TPoint) -> bool: ...
    def is_ever_within_distance(
        self, other: shpb.BaseGeometry | TPoint | STBox, distance: float
    ) -> bool: ...
    def ever_intersects(self, other: shpb.BaseGeometry | TPoint | STBox) -> bool: ...
    def ever_touches(self, other: shpb.BaseGeometry | STBox) -> bool: ...
    def is_spatially_contained_in(
        self, container: shpb.BaseGeometry | STBox
    ) -> TBool: ...
    def disjoint(self, other: shpb.BaseGeometry | STBox) -> TBool: ...
    def within_distance(
        self, other: shpb.BaseGeometry | TPoint | STBox, distance: float
    ) -> TBool: ...
    def intersects(self, other: shpb.BaseGeometry | STBox) -> TBool: ...
    def touches(self, other: shpb.BaseGeometry | STBox) -> TBool: ...
    def distance(self, other: shpb.BaseGeometry | TPoint | STBox) -> TFloat: ...
    def nearest_approach_distance(
        self, other: shpb.BaseGeometry | STBox | TPoint
    ) -> float: ...
    def nearest_approach_instant(self, other: shpb.BaseGeometry | TPoint) -> TI: ...
    def shortest_line(self, other: shpb.BaseGeometry | TPoint) -> shpb.BaseGeometry: ...
    def tile(
        self,
        size: float,
        duration: timedelta | str | None = None,
        origin: shpb.BaseGeometry | None = None,
        start: datetime | str | None = None,
        remove_empty: bool | None = False,
    ) -> list[TG]: ...
    def space_split(
        self,
        xsize: float,
        ysize: float | None = None,
        zsize: float | None = None,
        origin: shpb.BaseGeometry | None = None,
        bitmatrix: bool = False,
        include_border: bool = True,
    ) -> list[Temporal]: ...
    def space_time_split(
        self,
        xsize: float,
        duration: str | timedelta,
        ysize: float | None = None,
        zsize: float | None = None,
        origin: shpb.BaseGeometry | None = None,
        time_start: str | datetime | None = None,
        bitmatrix: bool = False,
        include_border: bool = True,
    ) -> list[Temporal]: ...

class TPointInst(
    TInstant[shpb.BaseGeometry, TG, TI, TS, TSS],
    TPoint[TG, TI, TS, TSS],
    ABC,
    metaclass=abc.ABCMeta,
):
    def value(self, precision: int = 15) -> shp.Point: ...
    def x(self) -> TFloatInst: ...
    def y(self) -> TFloatInst: ...
    def z(self) -> TFloatInst: ...

class TPointSeq(
    TSequence[shpb.BaseGeometry, TG, TI, TS, TSS],
    TPoint[TG, TI, TS, TSS],
    ABC,
    metaclass=abc.ABCMeta,
):
    def x(self) -> TFloatSeq: ...
    def y(self) -> TFloatSeq: ...
    def z(self) -> TFloatSeq: ...
    def plot(self, *args, **kwargs): ...

class TPointSeqSet(
    TSequenceSet[shpb.BaseGeometry, TG, TI, TS, TSS],
    TPoint[TG, TI, TS, TSS],
    ABC,
    metaclass=abc.ABCMeta,
):
    def to_dataframe(self, precision: int = 15) -> GeoDataFrame: ...
    def x(self) -> TFloatSeqSet: ...
    def y(self) -> TFloatSeqSet: ...
    def z(self) -> TFloatSeqSet: ...
    def plot(self, *args, **kwargs): ...

class TGeomPoint(
    TPoint["TGeomPoint", "TGeomPointInst", "TGeomPointSeq", "TGeomPointSeqSet"], ABC
):
    BaseClass: Incomplete
    @staticmethod
    def from_base_temporal(value: shpb.BaseGeometry, base: Temporal) -> TGeomPoint: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: datetime, interpolation: None = None
    ) -> TGeomPointInst: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: TsTzSet, interpolation: None = None
    ) -> TGeomPointSeq: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: TsTzSpan, interpolation: TInterpolation = None
    ) -> TGeomPointSeq: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry,
        base: TsTzSpanSet,
        interpolation: TInterpolation = None,
    ) -> TGeomPointSeqSet: ...
    @classmethod
    def from_mfjson(cls, mfjson: str) -> Self: ...
    def to_geographic(self) -> TGeogPoint: ...
    def to_dataframe(self) -> GeoDataFrame: ...
    def always_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def always_not_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def ever_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def ever_not_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def never_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def never_not_equal(self, value: shpb.BaseGeometry | TGeomPoint) -> bool: ...
    def is_ever_disjoint(
        self, other: shpb.BaseGeometry | TGeomPoint | STBox
    ) -> bool: ...
    def temporal_equal(self, other: shp.Point | TGeomPoint) -> TBool: ...
    def temporal_not_equal(self, other: shp.Point | TGeomPoint) -> TBool: ...
    @staticmethod
    def read_from_cursor(value, _: Incomplete | None = None): ...

class TGeogPoint(
    TPoint["TGeogPoint", "TGeogPointInst", "TGeogPointSeq", "TGeogPointSeqSet"], ABC
):
    BaseClass: Incomplete
    @staticmethod
    def from_base_temporal(value: shpb.BaseGeometry, base: Temporal) -> TGeogPoint: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: datetime, interpolation: TInterpolation = None
    ) -> TGeogPointInst: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: TsTzSet, interpolation: TInterpolation = None
    ) -> TGeogPointSeq: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry, base: TsTzSpan, interpolation: TInterpolation = None
    ) -> TGeogPointSeq: ...
    @staticmethod
    @overload
    def from_base_time(
        value: shpb.BaseGeometry,
        base: TsTzSpanSet,
        interpolation: TInterpolation = None,
    ) -> TGeogPointSeqSet: ...
    @classmethod
    def from_mfjson(cls, mfjson: str) -> Self: ...
    def to_geometric(self) -> TGeomPoint: ...
    def always_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def always_not_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def ever_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def ever_not_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def never_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def never_not_equal(self, value: shpb.BaseGeometry | TGeogPoint) -> bool: ...
    def temporal_equal(self, other: shp.Point | TGeogPoint) -> TBool: ...
    def temporal_not_equal(self, other: shp.Point | TGeogPoint) -> TBool: ...
    @staticmethod
    def read_from_cursor(value, _: Incomplete | None = None): ...

class TGeomPointInst(
    TPointInst["TGeomPoint", "TGeomPointInst", "TGeomPointSeq", "TGeomPointSeqSet"],
    TGeomPoint,
):
    def __init__(
        self,
        string: str | None = None,
        *,
        point: (
            str | shp.Point | tuple[float, float] | tuple[float, float, float] | None
        ) = None,
        timestamp: str | datetime | None = None,
        srid: int | None = 0,
        _inner: Incomplete | None = None,
    ) -> None: ...

class TGeogPointInst(
    TPointInst["TGeogPoint", "TGeogPointInst", "TGeogPointSeq", "TGeogPointSeqSet"],
    TGeogPoint,
):
    def __init__(
        self,
        string: str | None = None,
        *,
        point: (
            str | shp.Point | tuple[float, float] | tuple[float, float, float] | None
        ) = None,
        timestamp: str | datetime | None = None,
        srid: int | None = 4326,
        _inner: Incomplete | None = None,
    ) -> None: ...

class TGeomPointSeq(
    TPointSeq["TGeomPoint", "TGeomPointInst", "TGeomPointSeq", "TGeomPointSeqSet"],
    TGeomPoint,
):
    ComponentClass = TGeomPointInst
    def __init__(
        self,
        string: str | None = None,
        *,
        instant_list: list[str | TGeomPointInst] | None = None,
        lower_inc: bool = True,
        upper_inc: bool = False,
        interpolation: TInterpolation = ...,
        normalize: bool = True,
        _inner: Incomplete | None = None,
    ) -> None: ...

class TGeogPointSeq(
    TPointSeq["TGeogPoint", "TGeogPointInst", "TGeogPointSeq", "TGeogPointSeqSet"],
    TGeogPoint,
):
    ComponentClass = TGeogPointInst
    def __init__(
        self,
        string: str | None = None,
        *,
        instant_list: list[str | TGeogPointInst] | None = None,
        lower_inc: bool = True,
        upper_inc: bool = False,
        interpolation: TInterpolation = ...,
        normalize: bool = True,
        _inner: Incomplete | None = None,
    ) -> None: ...

class TGeomPointSeqSet(
    TPointSeqSet["TGeomPoint", "TGeomPointInst", "TGeomPointSeq", "TGeomPointSeqSet"],
    TGeomPoint,
):
    ComponentClass = TGeomPointSeq
    def __init__(
        self,
        string: str | None = None,
        *,
        sequence_list: list[str | TGeomPointSeq] | None = None,
        normalize: bool = True,
        _inner: Incomplete | None = None,
    ) -> None: ...

class TGeogPointSeqSet(
    TPointSeqSet["TGeogPoint", "TGeogPointInst", "TGeogPointSeq", "TGeogPointSeqSet"],
    TGeogPoint,
):
    ComponentClass = TGeogPointSeq
    def __init__(
        self,
        string: str | None = None,
        *,
        sequence_list: list[str | TGeogPointSeq] | None = None,
        normalize: bool = True,
        _inner: Incomplete | None = None,
    ) -> None: ...
