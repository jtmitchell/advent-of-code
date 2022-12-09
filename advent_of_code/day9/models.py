from __future__ import annotations

import math
from dataclasses import astuple, dataclass, field, fields


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
class Knot:
    """
    Class for the knot at the head or tail of the rope.
    """

    position: Vector
    trail: list[Vector] = field(default_factory=list)

    def move(self, translation: Vector) -> None:
        """
        Move the know and return new position.
        """
        self.trail.append(self.position)
        self.position += translation

    def follow(self, target: Vector) -> None:
        """
        Move to follow the target.
        """
        v_difference = target - self.position
        abs_difference = Vector(abs(v_difference.x), abs(v_difference.y))
        if abs_difference in [Vector(0, 0), Vector(1, 1), Vector(0, 1), Vector(1, 0)]:
            # no need to move
            return
        self.trail.append(self.position)
        move = Vector()
        if abs_difference.x >= 1:
            move.x = int(math.copysign(1, v_difference.x))
        if abs_difference.y >= 1:
            move.y = int(math.copysign(1, v_difference.y))

        self.position += move


@dataclass
class Rope:
    """
    Class for the rope bridge.
    """

    head: Knot
    tail: Knot
    is_test: bool = False

    def move(self, direction: str, steps: int) -> None:
        """
        Move the head, and have the tail follow, for each step.
        """
        translation = TRANSLATE.get(direction)
        assert translation is not None
        for _ in range(steps):
            self.head.move(translation)
            self.tail.follow(self.head.position)
            if self.is_test:
                print(
                    f"Move={direction}:{steps} "
                    f"Head={self.head.position} "
                    f"Tail={self.tail.position}"
                )


TRANSLATE = {
    "R": Vector(x=1, y=0),
    "L": Vector(x=-1, y=0),
    "U": Vector(x=0, y=1),
    "D": Vector(x=0, y=-1),
}
