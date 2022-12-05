import os
import re
from argparse import Namespace

from .models import StackOfCrates


def solve(args: Namespace):
    """
    Solve the stacking puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Crates")
    print(f"loading {input_file}")

    STACK_RE = re.compile(r"([ \[]?\w[ \]]?)")
    stacks: list[StackOfCrates] = []
    # building_stacks = True
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            line = line.strip()
            print(f"{STACK_RE.findall(line)}")

    print(f"Read {len(stacks)} assignments")

    # Puzzle 1
    # What crates are on top of the stacks?

    # Puzzle 2
