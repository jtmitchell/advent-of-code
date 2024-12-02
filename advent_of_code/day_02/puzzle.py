"""
Advent of Code Puzzle.
Day 2: Red-Nosed Reports
"""

import pathlib
from argparse import Namespace


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> list[list[int]]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    data = []
    with open(datafile, encoding="utf8") as fh:
        for line in fh:
            data.append(line.split())
    return data


def solve_pt1(data: list[list[int]]):
    """
    Solve the part one puzzle.
    """
    for report in data:
        pass


def solve_pt2(data: list[list[int]]):
    """
    Solve the part two puzzle.
    """
    return None
