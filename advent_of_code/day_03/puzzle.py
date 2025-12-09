"""
Advent of Code Puzzle.
Day 3: Lobby
"""

import pathlib
from argparse import Namespace
from collections.abc import Iterable
from pathlib import Path

from .models import PowerBank


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Iterable[PowerBank] = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Iterable[PowerBank]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            if value := line.strip():
                yield PowerBank(value=value)


def solve_pt1(data: Iterable[PowerBank]) -> int:
    """
    Solve the part one puzzle.
    """
    total_jotage = sum([i.jotage() for i in data])
    return total_jotage


def solve_pt2(data: Iterable[PowerBank]) -> int:
    """
    Solve the part two puzzle.
    """
    total_jotage = sum([i.jotage(batteries=12) for i in data])
    return total_jotage
