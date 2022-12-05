import os
from argparse import Namespace

from .models import Assignment, ElfPair


def solve(args: Namespace):
    """
    Solve the cleanup puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Calories")
    print(f"loading {input_file}")

    assignments = []
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            line = line.strip()
            (assignment1, assignment2) = line.split(",")
            assignments.append(
                ElfPair(
                    elf1=Assignment(assignment=assignment1),
                    elf2=Assignment(assignment=assignment2),
                )
            )

    full_overlaps = [i for i in assignments if i.is_full_overlap]
    partial_overlaps = [i for i in assignments if i.is_partial_overlap]

    print(f"Read {len(assignments)} assignments")

    # Puzzle 1
    # In how many assignment pairs does one range fully contain the other?-
    print(f"Number of fully overlapping assignments is {len(full_overlaps)}")

    # Puzzle 2
    print(f"Number of Partial overlapping assignments is {len(partial_overlaps)}")
