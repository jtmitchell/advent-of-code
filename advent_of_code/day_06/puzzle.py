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
        return self.in_room(location=self.guard_location)

    def in_room(self, location: Vector) -> bool:
        """
        Return True if the location is inside the room.
        """
        return all(
            [
                0 <= location.x < self.width,
                0 <= location.y < self.height,
            ]
        )

    @classmethod
    def rotate(cls, direction: Vector) -> Vector:
        """
        Rotate the direction 90 degrees.
        """
        return Vector(x=-direction.y, y=direction.x)

    @classmethod
    def move(cls, location: Vector, direction: Vector, distance: int = 1) -> Vector:
        """
        Return the new location after moving in the direction.
        """
        return location + (distance * direction)

    def move_guard(self, distance: int = 1) -> tuple[Vector, Vector]:
        """
        Move the guard and return the new location and direction.
        """

        new_location = self.move(
            location=self.guard_location, distance=distance, direction=self.guard_direction
        )

        if new_location in self.obstructions:
            # Rotate 90 degrees
            self.guard_direction = self.rotate(self.guard_direction)
        else:
            self.guard_location = new_location

        return self.guard_location, self.guard_direction


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
        visited.append(data.move_guard(distance=1)[0])

    distinct_locations = set(visited)
    return len(distinct_locations)


def solve_pt2(data: Room):
    """
    Solve the part two puzzle.
    """
    visited = [(data.guard_location, data.guard_direction)]
    while data.is_guard_in_room:
        visited.append(data.move_guard(distance=1))

    # Loop through each location.
    # Find where a 90 degree turn for the 2nd point gives the same direction as the 1st point.
    locations = {}
    block_location_list = []
    for location, direction in visited:
        if location in locations and Room.rotate(direction) in locations[location]:
            block_location = Room.move(location=location, direction=direction, distance=1)
            # Verify the BLOCK location is inside the map.
            if data.in_room(location=block_location):
                block_location_list.append(block_location)
        # Make a dict with location as the key
        if location in locations:
            locations[location].append(direction)
        else:
            locations[location] = [direction]

    # TODO find locations where a rotation will send the guard back to a previous path
    # but which is not an intersection, and there are no obstructions getting back to the path.

    return len(list(set(block_location_list)))
