"""
Advent of Code Puzzle.
Day 4: Printing Department
"""

import pathlib
from argparse import Namespace
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from utils.vector import Vector

from .models import Content, Room, RoomLocation


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Any = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Iterable[RoomLocation]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line_num, line in enumerate(fh):
            for position, i in enumerate(line.strip()):
                yield RoomLocation(content=i, location=Vector(x=position, y=line_num))


def solve_pt1(data) -> int:
    """
    Solve the part one puzzle.
    """
    room = Room(data=data)
    accessible = [i for i in room.locations.values() if i.is_paper() and room.is_accessible(i)]
    return len(accessible)


def solve_pt2(data) -> int:
    """
    Solve the part two puzzle.
    """
    room = Room(data=data)
    removed = 0
    do_loop = True
    while do_loop:
        # Find the locations with accessible paper rolls
        accessible = [
            i for i in room.locations.values() if i.is_paper() and room.is_accessible(i)
        ]

        # If there are no more accessible locations, we are finished
        if not accessible:
            break

        # Remove the accessible paper rolls
        for i in accessible:
            i.content = Content.EMPTY.value

        removed += len(accessible)

    return removed
