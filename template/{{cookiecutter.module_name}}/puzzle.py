"""
Advent of Code Puzzle.
Day {{cookiecutter.day_number}}: {{cookiecutter.puzzle_name}}
"""

import os
from argparse import Namespace


def solve(args: Namespace):
    """
    Solve the puzzle.
    """

    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)
    print(f"loading {input_file}")

    # Load the puzzle data
    with open(input_file, encoding="utf8") as fh:
        for line in fh.readlines():
            pass

    # Print the solution
