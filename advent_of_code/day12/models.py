from dataclasses import astuple, dataclass, field, fields
from typing import Optional


@dataclass
class Vector:
    """
    Class for the X/Y position.
    """

    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Vector(
            *(
                getattr(self, dim.name) + getattr(other, dim.name)
                for dim in fields(self)
            )
        )

    def __sub__(self, other):
        return Vector(
            *(
                getattr(self, dim.name) - getattr(other, dim.name)
                for dim in fields(self)
            )
        )

    def __mul__(self, other):
        return Vector(*(getattr(self, dim.name) * other for dim in fields(self)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class MapSquare:
    """
    Class for a square on the map.
    """

    location: Vector
    height: int
    is_start: bool = False
    is_end: bool = False


@dataclass
class Map:
    """
    Class to hold a map.
    """

    squares: list[MapSquare] = field(default_factory=list)


@dataclass
class RouteStep:
    """
    Class to hold a step on the route.
    """

    this_step: MapSquare
    last_step: Optional[MapSquare] = None
    next_step: Optional[MapSquare] = None


@dataclass
class Route:
    """
    Class to hold a route.
    """

    steps: list[RouteStep] = field(default_factory=list)
