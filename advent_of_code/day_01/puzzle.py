"""
Advent of Code Puzzle.
Day 1: Secret Entrance
"""

import pathlib
from argparse import Namespace
from collections.abc import Generator
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


def load_data(datafile: str) -> Generator[tuple[str, int], Any, None]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(file=datafile, encoding="utf8") as fh:
        for line in fh:
            if not line or line[0].upper() not in ["R", "L"]:
                continue
            direction: str = line[0].upper()
            rotations: int = int(line[1:])
            yield (direction, rotations)


def solve_pt1(data) -> int:
    """
    Solve the part one puzzle.

    Result is 1191
    """
    dial_number: int = 50
    dial_max: int = 100
    counter: int = 0
    for direction, rotation in data:
        if direction == "L":
            rotation = 0 - rotation

        delta: int = dial_number + rotation
        dial_number: int = delta % dial_max

        if dial_number == 0:
            counter += 1

    return counter


def solve_pt2(data) -> int:
    """
    Solve the part two puzzle.

    6835 is too low
    6951 is not correct
    """
    dial_number: int = 50
    dial_max: int = 100
    counter: int = 0
    for direction, rotation in data:
        if direction == "L":
            rotation = 0 - rotation

        delta: int = dial_number + rotation
        dial_number: int = delta % dial_max

        counter += abs(delta // dial_max)
        # if dial_number == 0 and abs(delta) < dial_max:
        #     counter += 1

    return counter
