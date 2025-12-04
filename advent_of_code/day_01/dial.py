"""
Dial dataclass to brute force the rotations.
"""

from dataclasses import dataclass


@dataclass
class Dial:
    position: int = 0
    min_pos: int = 0
    max_pos: int = 99
    zero_crossings: int = 0

    def rotate(self, direction: str, clicks: int) -> tuple[int, int]:
        """Rotate the dial position."""
        rotation = 1 if direction == "R" else -1
        crossings = 0

        for _ in range(clicks):
            old_pos = self.position
            self.position += rotation

            if self.position > self.max_pos:
                self.position = self.min_pos
            elif self.position < self.min_pos:
                self.position = self.max_pos

            if old_pos != self.min_pos and self.position == self.min_pos:
                crossings += 1

        self.zero_crossings += crossings

        return self.position, crossings
