"""
Advent of Code Puzzle.
Day 1: Historian Hysteria
"""

import os
from argparse import Namespace


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    data = load_data(input_file)

    # Print the solution
    pass


def load_data(datafile: str):
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    with open(datafile, encoding="utf8") as fh:
        for line in fh:
            pass


def solve(data):
    """
    Solve the puzzle.
    """
    return None
