"""
Advent of Code Puzzle.
Day 6: Guard Gallivant
"""

import pathlib
from argparse import Namespace
from dataclasses import dataclass, field

from utils.vector import Vector


@dataclass
class Room:
    height: int = 0
    width: int = 0
    obstructions: list[Vector] = field(default_factory=list)
    guard_location: Vector = field(default_factory=Vector)
    guard_direction: Vector = field(default_factory=Vector)

    @property
    def is_guard_in_room(self):
        return all(
            [
                0 <= self.guard_location.x < self.width,
                0 <= self.guard_location.y < self.height,
            ]
        )

    def move(self, distance: int = 1) -> list[Vector]:
        steps = []
        new_location = self.guard_location + (distance * self.guard_direction)
        if new_location in self.obstructions:
            # Rotate 90 degrees
            self.guard_direction = Vector(x=-self.guard_direction.y, y=self.guard_direction.x)
        else:
            self.guard_location = new_location
            steps.append(new_location)

        return steps


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Room:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    room = Room()
    with open(datafile, encoding="utf8") as fh:
        # Because I'm using enumerate for each line and character
        # my coordinate origin (0,0) is the TOP LEFT corner
        # with Y increasing DOWN the page
        for row, line in enumerate(fh):
            room.height = row
            for column, char in enumerate(line):
                room.width = column
                location = Vector(x=column, y=row)
                match char:
                    case "#":
                        room.obstructions.append(location)
                    case "^":
                        room.guard_location = location
                        room.guard_direction = Vector(x=0, y=-1)
                    case "<":
                        room.guard_location = location
                        room.guard_direction = Vector(x=-1, y=0)
                    case ">":
                        room.guard_location = location
                        room.guard_direction = Vector(x=1, y=0)
                    # Not sure what a downward pointing char is...
                    case _:
                        pass

    return room


def solve_pt1(data: Room):
    """
    Solve the part one puzzle.
    """
    visited = []
    while data.is_guard_in_room:
        visited.extend(data.move(distance=1))

    distinct_locations = set(visited)
    return len(distinct_locations)


def solve_pt2(data: Room):
    """
    Solve the part two puzzle.
    """
    return None
