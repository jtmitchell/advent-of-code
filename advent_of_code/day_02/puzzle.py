"""
Advent of Code Puzzle.
Day 2: Red-Nosed Reports
"""

import pathlib
from argparse import Namespace

from utils.grouper import grouper

INCREASE = "increase"
DECREASE = "decrease"


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
            data.append([int(i) for i in line.split()])
    return data


def solve_pt1(data: list[list[int]]) -> int:
    """
    Solve the part one puzzle.
    """
    count_safe = 0

    for report in data:
        report_safe = True
        report_trend = None
        for l1, l2 in grouper(report, 2):
            if report_trend is None:
                report_trend = INCREASE if l2 > l1 else DECREASE
            else:
                if report_trend == INCREASE and not (l2 > l1):
                    report_safe = False
                    break
            level_diff = abs(l1 - l2)
            if level_diff > 3 or level_diff < 1:
                report_safe = False
                break
        if report_safe:
            count_safe += 1
    return count_safe


def solve_pt2(data: list[list[int]]):
    """
    Solve the part two puzzle.
    """
    return None
