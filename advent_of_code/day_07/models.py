"""
Models for Day 7: Laboratories.
"""

from dataclasses import dataclass

from utils.vector import Vector


@dataclass
class Room:
    start_pt: Vector | None = None
    splitters: list[Vector] | None = None
    beams: set[Vector] | None = None
    beam_counter: int = 0
    max_x: int = 0
    max_y: int = 0

    def __post_init__(self):
        if self.splitters is None:
            self.splitters = []

        if self.beams is None:
            self.beams = set()

    def add_line(self, line: str, line_num: int) -> None:
        self.max_y = line_num
        for key, value in enumerate(line):
            this_pt = Vector(x=key, y=line_num)
            if key > self.max_x:
                self.max_x = key

            match value:
                case "S":
                    self.start_pt = this_pt
                case "^":
                    self.splitters.append(this_pt)
                case _:
                    pass

    def activate_beam(self):
        self.beams.add(self.start_pt)
        for point in self.beams:
            next_pt, new_beams = self.move_beam(start_pt=point)

    def move_beam(self, start_pt: Vector) -> tuple[Vector | None, set[Vector]]:
        delta_y = Vector(x=0, y=-1)
        next_pt = start_pt + delta_y
        new_beams = set()

        if next_pt.y < 0:
            # Reached the bottom
            return None, new_beams

        if next_pt in self.splitters:
            # Split the beam and check the new start points
            for delta_x in [Vector(x=-1, y=0), Vector(x=1, y=0)]:
                new_beam_start = next_pt + delta_x
                if any(
                    [
                        new_beam_start.x < 0,
                        new_beam_start >= self.max_x,
                        new_beam_start in self.splitters,
                    ]
                ):
                    # Ignore anything that is outside the room
                    continue

                new_beams.add(new_beam_start)

        return next_pt, new_beams
