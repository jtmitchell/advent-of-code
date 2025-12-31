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
        return self.unique_beams()

    def unique_beams(self) -> int:
        """
        Discard any overlapping beams.
        """
        # Sort the beams into columns
        beam_cols = {}
        for i in self.beams:
            key = i.start.x
            if key not in beam_cols:
                beam_cols[key] = []
            beam_cols[key].append(i)

        # Find overlapping beams
        unique_beams = []
        for i in self.beams:
            key = i.start.x
            found = False
            for j in sorted(beam_cols[key], key=lambda x: (x.start.y, x.end.y)):
                if i.start == j.start and i.end == j.end:
                    # Skip the entry for this beam
                    continue
                if j.start.y <= i.start.y and i.end.y <= j.end.y:
                    # Overlapping beams
                    found = True
                    break
            if not found:
                unique_beams.append(i)

        return len(unique_beams)

    def emit_beam(self, start_pt: Vector) -> list[BeamPath]:
        delta_y = Vector(x=0, y=1)
        beam = BeamPath(start=start_pt, end=start_pt)
        new_beams = [beam]
        do_next_step = True

        while do_next_step:
            beam.end += delta_y
            if beam.end.y >= self.max_y:
                # Reached the bottom
                do_next_step = False

            elif beam.end in self.splitters:
                # Split the beam and check the new start points
                for delta_x in [Vector(x=-1, y=0), Vector(x=1, y=0)]:
                    new_beam_start = beam.end + delta_x
                    if any(
                        [
                            new_beam_start.x < 0,
                            new_beam_start.x >= self.max_x,
                            new_beam_start in self.splitters,
                        ]
                    ):
                        # Ignore anything that is outside the room
                        continue

                    new_beams.extend(self.emit_beam(start_pt=new_beam_start))
                do_next_step = False

        return list(set(new_beams))
