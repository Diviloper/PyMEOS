from .aggregators import *
from .boxes import *
from .main import *
from .meos_init import *
from .temporal import *
from .collections import *
from pymeos_cffi import (
    MeosException,
    MeosInternalError,
    MeosArgumentError,
    MeosIoError,
    MeosInternalTypeError,
    MeosValueOutOfRangeError,
    MeosDivisionByZeroError,
    MeosMemoryAllocError,
    MeosAggregationError,
    MeosDirectoryError,
    MeosFileError,
    MeosInvalidArgError,
    MeosInvalidArgTypeError,
    MeosInvalidArgValueError,
    MeosMfJsonInputError,
    MeosMfJsonOutputError,
    MeosTextInputError,
    MeosTextOutputError,
    MeosWkbInputError,
    MeosWkbOutputError,
    MeosGeoJsonInputError,
    MeosGeoJsonOutputError,
)

__version__ = "1.1.4"
__all__ = [
    # initialization
    "pymeos_initialize",
    "pymeos_finalize",
    # boxes
    "Box",
    "TBox",
    "STBox",
    # main
    "TBool",
    "TBoolInst",
    "TBoolSeq",
    "TBoolSeqSet",
    "TInt",
    "TIntInst",
    "TIntSeq",
    "TIntSeqSet",
    "TFloat",
    "TFloatInst",
    "TFloatSeq",
    "TFloatSeqSet",
    "TText",
    "TTextInst",
    "TTextSeq",
    "TTextSeqSet",
    "TPointInst",
    "TPointSeq",
    "TPointSeqSet",
    "TGeomPoint",
    "TGeomPointInst",
    "TGeomPointSeq",
    "TGeomPointSeqSet",
    "TGeogPoint",
    "TGeogPointInst",
    "TGeogPointSeq",
    "TGeogPointSeqSet",
    # temporal
    "Temporal",
    "TInstant",
    "TSequence",
    "TSequenceSet",
    # Collections
    "Time",
    "TsTzSpan",
    "TsTzSet",
    "TsTzSpanSet",
    "TextSet",
    "IntSet",
    "IntSpan",
    "IntSpanSet",
    "FloatSet",
    "FloatSpan",
    "FloatSpanSet",
    "GeoSet",
    "GeometrySet",
    "GeographySet",
    # extras
    "TInterpolation",
    # aggregators
    "TemporalInstantCountAggregator",
    "TemporalPeriodCountAggregator",
    "TemporalExtentAggregator",
    "TemporalAndAggregator",
    "TemporalOrAggregator",
    "TemporalAverageAggregator",
    "TemporalNumberExtentAggregator",
    "TemporalIntMaxAggregator",
    "TemporalIntMinAggregator",
    "TemporalIntSumAggregator",
    "TemporalFloatMaxAggregator",
    "TemporalFloatMinAggregator",
    "TemporalFloatSumAggregator",
    "TemporalTextMaxAggregator",
    "TemporalTextMinAggregator",
    "TemporalPointExtentAggregator",
    "TimeInstantaneousUnionAggregator",
    "TimeContinuousUnionAggregator",
    # exceptions
    "MeosException",
    "MeosInternalError",
    "MeosArgumentError",
    "MeosIoError",
    "MeosInternalTypeError",
    "MeosValueOutOfRangeError",
    "MeosDivisionByZeroError",
    "MeosMemoryAllocError",
    "MeosAggregationError",
    "MeosDirectoryError",
    "MeosFileError",
    "MeosInvalidArgError",
    "MeosInvalidArgTypeError",
    "MeosInvalidArgValueError",
    "MeosMfJsonInputError",
    "MeosMfJsonOutputError",
    "MeosTextInputError",
    "MeosTextOutputError",
    "MeosWkbInputError",
    "MeosWkbOutputError",
    "MeosGeoJsonInputError",
    "MeosGeoJsonOutputError",
]