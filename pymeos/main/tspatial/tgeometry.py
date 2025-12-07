from typing import TYPE_CHECKING

from pymeos_cffi import tgeometry_to_tgeography, tgeometry_to_tgeompoint

from .tgeo import TGeo

if TYPE_CHECKING:
    from .tgeography import TGeography
    from .tgeompoint import TGeometricPoint


class TGeometry(TGeo):
    def to_tgeography(self) -> TGeography:
        from pymeos.factory import _TemporalFactory

        return _TemporalFactory.create_temporal(tgeometry_to_tgeography(self._inner))

    def to_tgeompoint(self) -> TGeometricPoint:
        from pymeos.factory import _TemporalFactory

        return _TemporalFactory.create_temporal(tgeometry_to_tgeompoint(self._inner))
