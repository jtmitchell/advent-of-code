"""
Advent of Code Puzzle.
Day 2: Red-Nosed Reports
"""

import pathlib
from argparse import Namespace

from utils import pairwise

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
            report = [int(i) for i in line.split()]
            if report:
                data.append(report)
    return data


def solve_pt1(data: list[list[int]]) -> int:
    """
    Solve the part one puzzle.
    """
    count_safe = 0

    for report in data:
        report_safe = True
        report_trend = None
        for l1, l2 in pairwise(report, 2):
            if report_trend is None:
                report_trend = INCREASE if l2 > l1 else DECREASE
            else:
                if report_trend == INCREASE and not (l2 > l1):
                    report_safe = False
                    break
                elif report_trend == DECREASE and not (l2 < l1):
                    report_safe = False
                    break
            level_diff = abs(l1 - l2)
            if level_diff > 3 or level_diff < 1:
                report_safe = False
                break
        if report_safe:
            count_safe += 1
    return count_safe


def solve_pt2(data: list[list[int]]) -> int:  # noqa: C901
    """
    Solve the part two puzzle.
    """

    def check_report(report: list[int]) -> tuple[bool, int]:
        """
        Check the report for safety.
        """
        report_safe = True
        report_trend = None
        for idx, (l1, l2) in enumerate(pairwise(report, 2)):
            if report_trend is None:
                report_trend = INCREASE if l2 > l1 else DECREASE
            else:
                if report_trend == INCREASE and not (l2 > l1):
                    return False, idx
                elif report_trend == DECREASE and not (l2 < l1):
                    return False, idx
                elif l1 == l2:
                    return False, idx

            level_diff = abs(l1 - l2)
            if level_diff > 3 or level_diff < 1:
                return False, idx
        return report_safe, idx

    count_safe = 0

    for report in data:
        # must loop through the report levels
        is_safe, idx = check_report(report)
        if is_safe:
            count_safe += 1
            continue
        # if there is an unsafe result, then we have to
        # loop through the report without the current item
        # if this is safe, we are good, if there is another unsafe, it fails
        filter_report = [v for (i, v) in enumerate(report) if i != idx]
        is_safe, _ = check_report(filter_report)
        if is_safe:
            count_safe += 1

        if idx == 1:
            # Also try removing the first element
            filter_report = report[1:]
            is_safe, _ = check_report(filter_report)
            if is_safe:
                count_safe += 1

        if idx == (len(report) - 2):
            # Also try removing the first element
            filter_report = report[:-1]
            is_safe, _ = check_report(filter_report)
            if is_safe:
                count_safe += 1

    return count_safe
