"""
Advent of Code Puzzle.
Day 5: Cafeteria
"""

import pathlib
from argparse import Namespace
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from advent_of_code.day_05.models import FreshFruit


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
    stock_list = FreshFruit()
    counter = 0
    for line in data:
        if "-" in line:
            start, stop = line.split("-")
            stock_list.add_range(range=(int(start), int(stop) + 1))
        elif line:
            id = int(line)
            counter += 1 if stock_list.is_fresh(id) else 0

    return counter


def solve_pt2(data: list[str]) -> int:
    """
    Solve the part two puzzle.
    """
    return None
