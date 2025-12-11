"""
Models for Day 04.
"""

from dataclasses import dataclass, field
from enum import Enum

from utils.vector import Vector


class Content(Enum):
    EMPTY = "."
    PAPER = "@"


@dataclass
class RoomLocation:
    location: Vector
    content: str

    def is_paper(self) -> bool:
        """Return True if the content is a paper roll."""
        return self.content == Content.PAPER.value


@dataclass
class Room:
    locations: list[RoomLocation] = field(default_factory=list)
    _map: dict | None = None
    max_x: int = 0
    max_y: int = 0

    def scan(self) -> None:
        self._map = {}
        for i in self.locations:
            x_pos = i.location.x
            y_pos = i.location.y
            if x_pos not in self._map:
                self._map[x_pos] = {}

            if x_pos > self.max_x:
                self.max_x = x_pos
            if y_pos > self.max_y:
                self.max_y = y_pos

            self._map[x_pos][y_pos] = i.content

    def is_accessible(
        self,
        location: RoomLocation,
        content: Content = Content.PAPER,
        limit: int = 4,
    ) -> bool:
        """Return True if the location has fewer than 4 paper rolls surrounding it."""
        if self._map is None:
            self.scan()

        possible_neighbour_locations = [
            i
            for i in self.neighbours(location=location)
            if all(
                [
                    0 <= i.x <= self.max_x,
                    0 <= i.y <= self.max_y,
                ]
            )
        ]
        neighbours_with_paper = [
            i
            for i in possible_neighbour_locations
            if self._map[i.x][i.y] == Content.PAPER.value
        ]
        return len(neighbours_with_paper) < limit

    def neighbours(self, location: RoomLocation) -> list[RoomLocation | None]:
        """Return a list of the neighbouring locations."""
        target = location.location
        offset = [
            Vector(x=-1, y=-1),
            Vector(x=0, y=-1),
            Vector(x=1, y=-1),
            Vector(x=-1, y=0),
            Vector(x=1, y=0),
            Vector(x=-1, y=1),
            Vector(x=0, y=1),
            Vector(x=1, y=1),
        ]
        neighbours = [target + i for i in offset]
        return neighbours
