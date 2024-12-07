"""
Definition of a Vector class.
"""

from dataclasses import astuple, dataclass, fields
from typing import Self


@dataclass(unsafe_hash=True)
class Vector:
    """
    Class for the X/Y position.
    """

    x: int = 0
    y: int = 0

    def __add__(self, other: Self) -> Self:
        return Vector(
            *(getattr(self, dim.name) + getattr(other, dim.name) for dim in fields(self))
        )

    def __sub__(self, other: Self) -> Self:
        return Vector(
            *(getattr(self, dim.name) - getattr(other, dim.name) for dim in fields(self))
        )

    def __mul__(self, other: Self) -> Self:
        return Vector(*(getattr(self, dim.name) * other for dim in fields(self)))

    def __rmul__(self, other: Self) -> Self:
        return self.__mul__(other)

    def __iter__(self):
        return iter(astuple(self))
