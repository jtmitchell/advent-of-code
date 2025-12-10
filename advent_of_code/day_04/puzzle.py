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

from .models import RoomLocation


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
                yield RoomLocation(content=i, location=Vector(x=line_num, y=position))


def solve_pt1(data) -> int:
    """
    Solve the part one puzzle.
    """
    room_locations = list(data)
    accessible = [i for i in room_locations if i.is_paper() and i.is_accessible()]
    return len(accessible)


def solve_pt2(data) -> int:
    """
    Solve the part two puzzle.
    """
    return None
