"""
Advent of Code Puzzle.
Day 1: Historian Hysteria
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


def load_data(datafile: str) -> tuple[list[int], list[int]]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    column1 = []
    column2 = []
    with open(datafile, encoding="utf8") as fh:
        for line in fh:
            c1, c2 = line.split()
            column1.append(int(c1))
            column2.append(int(c2))
    return column1, column2


def solve_pt1(data: tuple[list[int], list[int]]) -> int:
    """
    Solve the Part One puzzle.
    """
    result = 0
    column_1 = sorted(data[0])
    column_2 = sorted(data[1])
    for c1, c2 in zip(column_1, column_2, strict=True):
        result += abs(c1 - c2)
    return result


def solve_pt2(data: tuple[list[int], list[int]]) -> int:
    """
    Solve the Part Two puzzle.
    """
    result = 0
    column_1 = sorted(data[0])
    column_2 = sorted(data[1])
    for c1 in column_1:
        count_appears = [1 for c2 in column_2 if c1 == c2]
        result += c1 * len(count_appears)
    return result
