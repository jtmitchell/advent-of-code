import os
from argparse import Namespace

# from .models import Monkey, Troop


def solve(args: Namespace):
    """
    Solve the monkey puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Hill climbing")
    print(f"loading {input_file}")

    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            # Each line is a row of the map
            line = line.strip()

    # Puzzle 1
    # What is the fewest steps required to move from your current position to the location
    # that should get the best signal?

    # Puzzle 2
