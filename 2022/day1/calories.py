#!/usr/bin/env python3
import os
import argparse

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

elves = []
with open(input_file, "r", encoding="utf8") as fh:
    calories = 0
    for line in fh.readlines():
        line = line.strip()
        if line:
            calories += int(line)
        else:
            elves.append(calories)
            calories = 0

    # grab the last elf total
    elves.append(calories)

# Puzzle 1
# How many calories are all the elves carrying?
print(f"Elf total calories {elves}")
print(f"Number of elves: {len(elves)}")
print(f"Max calories: {max(elves)}")

# Puzzle 2
# How many calories are carried by the 3 elves who are carrying the most?
sorted_elves = sorted(elves, reverse=True)
top_three = sorted_elves[:3]

print(f"Elf sorted by calories {sorted_elves}")
print(f"Top 3 elves {top_three}")
print(f"Top 3 are carying {sum(top_three)}")
