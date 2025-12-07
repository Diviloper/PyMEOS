from __future__ import annotations

from typing import TypeAlias

from pymeos_cffi import (
    cbuffer_as_ewkt,
    cbuffer_as_hexwkb,
    cbuffer_as_text,
    cbuffer_as_wkb,
    cbuffer_from_wkb,
    cbuffer_hash,
    cbuffer_point,
    cbuffer_radius,
    cbuffer_to_geom,
    cbuffer_to_stbox,
    geom_to_cbuffer,
)

from ...boxes import STBox
from .geometry import Geometry
from .point import Point


class CircularBuffer:
    __slots__ = ["_inner"]

    _mobilitydb_name = "cbuffer"

    def __init__(self, _inner):
        self._inner = _inner

    # ------------------------- Input ----------------------------------------

    @staticmethod
    def from_geometry(geom: Geometry) -> CircularBuffer:
        """
        Creates a circular buffer from a geometry.

        Args:
            geom (Geometry): The geometry to create the circular buffer from.

        Returns:
            CircularBuffer: The circular buffer created from the geometry.
        """
        return CircularBuffer(_inner=geom_to_cbuffer(geom._inner))

    @staticmethod
    def from_wkb(wkb: bytes) -> CircularBuffer:
        """
        Creates a circular buffer from a Well-Known Binary (WKB) representation.

        Args:
            wkb (bytes): The WKB representation of the geometry.

        Returns:
            CircularBuffer: The circular buffer created from the geometry.
        """
        return CircularBuffer(_inner=cbuffer_from_wkb(wkb))

    # ------------------------- Output ----------------------------------------

    def as_text(self, max_digits: int = 15) -> str:
        """
        Returns the Well-Known Text (WKT) representation of the circular buffer.


        Args:
            max_digits (int): The maximum number of digits to include in the
                string representation.

        Returns:
            str: A string representation of the circular buffer,
            truncated to the specified number of digits.
        """
        return cbuffer_as_text(self._inner, max_digits)

    def as_ewkt(self, max_digits: int = 15) -> str:
        """
        Returns the EWKT (Extended Well-Known Text) representation of the circular buffer.

        Args:
            max_digits (int): Maximum number of decimal digits to include in the
                numeric coordinates of the geometry. Defaults to 15 if not provided.

        Returns:
            str: EWKT representation of the geometry.
        """
        return cbuffer_as_ewkt(self._inner, max_digits)

    def as_hexwkb(self, variant: int) -> str:
        """
        Returns the ASCII hex-encoded Well-Known Binary (HexWKB) representation of the circular buffer.

        Args:
            variant (int): An integer specifying the variant for HexWKB generation.

        Returns:
            str: The HexWKB representation of the geometry as a string.
        """
        return cbuffer_as_hexwkb(self._inner, variant)

    def as_wkb(self, variant: int) -> bytes:
        """
        Returns the Well-Known Binary (WKB) representation of the circular buffer.

        Args:
            variant (int): An integer specifying the variant for WKB generation.

        Returns:
            bytes: The WKB representation of the geometry as bytes.
        """
        return cbuffer_as_wkb(self._inner, variant)

    def as_geometry(self) -> Geometry:
        """
        Returns the geometry representation of the circular buffer.

        Returns:
            Geometry: The geometry representation of the circular buffer.
        """
        return Geometry(_inner=cbuffer_to_geom(self._inner))

    def __str__(self):
        """
        Returns the string representation of the circular buffer.

        Returns:
            str: The string representation of the circular buffer.
        """
        return self.as_text()

    def __hash__(self) -> int:
        """
        Returns the hash value of the circular buffer.

        Returns:
            int: The hash value of the circular buffer.
        """
        return cbuffer_hash(self._inner)

    # ------------------------- Accessors ----------------------------------------

    def radius(self) -> float:
        """
        Returns the radius of the circular buffer.

        Returns:
            float: The radius of the circular buffer.
        """
        return cbuffer_radius(self._inner)

    def center(self) -> Point:
        """
        Returns the center point of the circular buffer.

        Returns:
            Point: The center point of the circular buffer.
        """
        return Point(cbuffer_point(self._inner))

    def bounding_box(self) -> STBox:
        """
        Returns the bounding box of the circular buffer.

        Returns:
            STBox: The bounding box of the circular buffer.
        """
        return STBox(_inner=cbuffer_to_stbox(self._inner))


CBuffer: TypeAlias = CircularBuffer
