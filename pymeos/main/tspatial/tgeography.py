from typing import TYPE_CHECKING

from pymeos_cffi import tgeography_to_tgeogpoint, tgeography_to_tgeometry

from .tgeo import TGeo

if TYPE_CHECKING:
    from .tgeogpoint import TGeographicPoint
    from .tgeometry import TGeometry


class TGeography(TGeo):
    def to_tgeometry(self) -> TGeometry:
        from pymeos.factory import _TemporalFactory

        return _TemporalFactory.create_temporal(tgeography_to_tgeometry(self._inner))

    def to_tgeogpoint(self) -> TGeographicPoint:
        from pymeos.factory import _TemporalFactory

        return _TemporalFactory.create_temporal(tgeography_to_tgeogpoint(self._inner))
