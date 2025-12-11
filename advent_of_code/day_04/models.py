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

    def is_accessible(
        self,
        location: RoomLocation,
        content: Content = Content.PAPER,
        limit: int = 4,
    ) -> bool:
        """Return True if the location has fewer than 4 paper rolls surrounding it."""
        neighbour_locations = self.neighbours(location=location)
        accessible_locations = [
            i
            for i in self.locations
            if i.content == content.value and i.location in neighbour_locations
        ]
        return len(accessible_locations) < limit

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
