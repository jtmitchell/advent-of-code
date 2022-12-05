#!/usr/bin/env python3
import os
import argparse
from .models import Assignment, ElfPair

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--test", help="Run against the test data", action="store_true"
)
args = parser.parse_args()

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
