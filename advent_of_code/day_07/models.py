"""
Models for Day 7: Laboratories.
"""

from dataclasses import astuple, dataclass, field

from utils.vector import Vector


@dataclass(unsafe_hash=True)
class BeamPath:
    start: Vector | None = None
    end: Vector | None = None

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class Room:
    start_pt: Vector | None = None
    splitters: list[Vector] = field(default_factory=list)
    beams: set[BeamPath] = field(default_factory=set)
    max_x: int = 0
    max_y: int = 0

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

    def activate_beam(self) -> int:
        self.beams = self.emit_beam(start_pt=self.start_pt)
        return len(self.beams)

    def emit_beam(self, start_pt: Vector) -> set[BeamPath]:
        delta_y = Vector(x=0, y=-1)
        next_pt = start_pt + delta_y
        new_beams = set(BeamPath(start=start_pt))

        if next_pt.y < 0:
            # Reached the bottom
            return new_beams

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

                new_beams.union(self.emit_beam(start_pt=new_beam_start))

        return new_beams
