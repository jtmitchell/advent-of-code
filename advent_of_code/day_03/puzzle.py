"""
Advent of Code Puzzle.
Day 03: Mull It Over
"""

import pathlib
import re
from argparse import Namespace

MUL_STATEMENT = r"mul\((?P<num_x>\d{1,3}),(?P<num_y>\d{1,3})\)"
MUL_RX = re.compile(MUL_STATEMENT)

BETWEEN_START_STOP = re.compile(
    rf"(?=do\(\))(.*?)(?=don't\(\))"
)  # everything between a START and a STOP


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> str:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(datafile, encoding="utf8") as fh:
        data = fh.read()
    return data or ""


def solve_pt1(data: str) -> int:
    """
    Solve the part one puzzle.
    """
    total = 0
    for num_x, num_y in MUL_RX.findall(data):
        total += int(num_x) * int(num_y)
    return total


def solve_pt2(data: str):
    """
    Solve the part two puzzle.
    """
    total = 0
    data = "".join([i.strip() for i in data])
    for line in BETWEEN_START_STOP.findall(rf"do(){data}don't()"):
        for num_x, num_y in MUL_RX.findall(line):
            total += int(num_x) * int(num_y)
    return total
