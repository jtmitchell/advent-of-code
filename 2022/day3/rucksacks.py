#!/usr/bin/env python3
import os
import argparse
from models import Rucksack


parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--test", help="Run against the test data", action="store_true"
)
args = parser.parse_args()

dirname = os.path.dirname(__file__)
basefile = "sample.txt" if args.test else "input.txt"
input_file = os.path.join(dirname, basefile)

print("Rucksacks")
print(f"loading {input_file}")

rucksacks = []
with open(input_file, "r", encoding="utf8") as fh:
    calories = 0
    for line in fh.readlines():
        line = line.strip()
        rucksacks.append(Rucksack(items=line))

print(f"There are {len(rucksacks)}")
for num, r in enumerate(rucksacks,start=1):
    print(f"Bag{num} {r.compartment1} :: {r.compartment2} // shared {r.shared_items} // priority {r.priority}")

# Puzzle 1
# What is the sum of the priorities of the misplaced items
total_priorities = sum([r.priority for r in rucksacks])
print(f"Sum of priorities is {total_priorities}")

# Puzzle 2
