"""
Advent of Code Puzzle.
Day {{cookiecutter.day_number}}: {{cookiecutter.puzzle_name}}
"""

import pathlib
from argparse import Namespace
from pathlib import Path
from typing import Any


def run_puzzle(args: Namespace) -> None:
    """
    Run the puzzle.
    """

    input_file: Path = pathlib.Path(__file__).with_name(name="input.txt")
    data: Any = load_data(datafile=input_file)

    # Print the solution
    result: bool = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> Any:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            line.split()


def solve_pt1(data) -> bool:
    """
    Solve the part one puzzle.
    """
    return False


def solve_pt2(data) -> bool:
    """
    Solve the part two puzzle.
    """
    return False
