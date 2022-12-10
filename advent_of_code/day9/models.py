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

    @property
    def all_positions(self) -> list[Vector]:
        """
        Get the list of all positions.
        """
        return self.trail + [self.position]

    @property
    def unique_positions(self) -> list[Vector]:
        """
        Get a list of unique positions.
        """
        unique_pos = {(x.x, x.y) for x in self.all_positions}
        return [Vector(x=x[0], y=x[1]) for x in unique_pos]

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

    knots: list[Knot] = field(default_factory=list)
    is_test: bool = False

    @property
    def head(self) -> Knot:
        """
        Return the head of the rope.
        """
        return self.knots[0]

    @property
    def tail(self) -> Knot:
        """
        Return the tail of the rope.
        """
        return self.knots[-1]

    def move(self, direction: str, steps: int) -> None:
        """
        Move the head, and have the tail follow, for each step.
        """
        translation = TRANSLATE.get(direction)
        assert translation is not None
        for _ in range(steps):
            # Move the head of the rope
            self.head.move(translation)

            for i in range(1, len(self.knots)):
                # Make each subsequent knot follow the previous one
                head = self.knots[i - 1]
                tail = self.knots[i]
                tail.follow(head.position)
                if self.is_test:
                    print(
                        f"Move={direction}:{steps} "
                        f"knot[{i-1}]={head.position} "
                        f"knot[{i}]={tail.position}"
                    )


TRANSLATE = {
    "R": Vector(x=1, y=0),
    "L": Vector(x=-1, y=0),
    "U": Vector(x=0, y=1),
    "D": Vector(x=0, y=-1),
}
