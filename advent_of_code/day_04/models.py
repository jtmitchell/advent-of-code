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
    locations: dict[Vector, RoomLocation] = field(default_factory=dict)

    def is_accessible(
        self,
        location: RoomLocation,
        content: Content = Content.PAPER,
        limit: int = 4,
    ) -> bool:
        """Return True if the location has fewer than 4 paper rolls surrounding it."""

        possible_neighbour_locations = self.neighbours(location=location)
        neighbours_with_paper = [
            loc
            for loc in possible_neighbour_locations
            if loc in self.locations and self.locations[loc].content == content.value
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
