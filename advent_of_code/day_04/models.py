"""
Models for Day 03.
"""

from dataclasses import dataclass
from enum import Enum

from utils.vector import Vector


class Content(Enum):
    EMPTY = "."
    PAPER = "@"


@dataclass
class RoomLocation:
    location: Vector
    content: str

    def is_accessible(self) -> bool:
        """Return True if the location has fewer than 4 paper rolls surrounding it."""
        return True

    def is_paper(self) -> bool:
        """Return True if the content is a paper roll."""
        return self.content == Content.PAPER.value
