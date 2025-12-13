"""
Advent of Code Puzzle.
Day 6: Trash Compactor
"""

import pathlib
from argparse import Namespace
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .models import Equations


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Any = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Iterable[list[str]]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            yield line.strip().split()


def solve_pt1(data) -> int:
    """
    Solve the part one puzzle.
    """
    equations = Equations()
    for line in data:
        if line:
            equations.add_line(line)

    return equations.get_total()


def solve_pt2(data) -> int:
    """
    Solve the part two puzzle.
    """
    return None
