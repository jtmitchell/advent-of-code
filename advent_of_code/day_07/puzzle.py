"""
Advent of Code Puzzle.
Day 7: Laboratories
"""

import pathlib
from argparse import Namespace
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .models import Room


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Any = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Iterable[str]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            yield line.strip()


def solve_pt1(data: list[str]) -> int:
    """
    Solve the part one puzzle.
    """
    room = Room()

    for line_num, line in enumerate(data):
        room.add_line(line=line, line_num=line_num)

    return None


def solve_pt2(data: list[str]) -> int:
    """
    Solve the part two puzzle.
    """
    return None
