import os
from argparse import Namespace

from .models import Buffer


def solve(args: Namespace):
    """
    Solve the radio tuner puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Tuner")
    print(f"loading {input_file}")

    buffer_size = 14 if args.newrules else 4
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            line = line.strip()
            print(f"Input {line}")
            buffer = Buffer(size=buffer_size)
            for i, char in enumerate(line, start=1):
                print(char, end="")
                if buffer.add(char):
                    print(f"\nMarker at position {i}")
                    break

    # Puzzle 1
    # how many characters before first start-of-packet marker (4 chars)

    # Puzzle 2
    # how many characters before first start-of-message marker (14 chars)
