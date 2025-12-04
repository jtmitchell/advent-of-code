"""
Advent of Code Puzzle.
Day 2: Gift Shop
"""

import pathlib
from argparse import Namespace
from pathlib import Path
from typing import Any, Iterator


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Any = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Iterator[tuple[int, int]]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            for item in line.split(sep=","):
                i = item.split(sep="-")
                yield (int(i[0]), int(i[1]))


def solve_pt1(data: list[tuple[int, int]]) -> bool:
    """
    Solve the part one puzzle.
    """
    from .product import Product

    counter = 0
    for start, end in data:
        for i in range(start, end + 1):
            p = Product(id=i)
            counter += 0 if p.is_valid() else p.id

    return counter


def solve_pt2(data) -> bool:
    """
    Solve the part two puzzle.
    """
    return False
