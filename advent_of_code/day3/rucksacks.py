import os
from argparse import Namespace

from .models import PRIORITIES, Rucksack
from advent_of_code.utils import grouper


def solve(args: Namespace):
    """
    Solve the rucksacks puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Rucksacks")
    print(f"loading {input_file}")

    rucksacks = []
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            line = line.strip()
            rucksacks.append(Rucksack(items=line))

    print(f"There are {len(rucksacks)}")
    for num, r in enumerate(rucksacks, start=1):
        print(
            f"Bag{num} {r.compartment1} :: {r.compartment2} "
            f"// shared {r.shared_items} // priority {r.priority}"
        )

    # Puzzle 1
    # What is the sum of the priorities of the misplaced items
    total_priorities = sum([r.priority for r in rucksacks])
    print(f"Sum of priorities is {total_priorities}")

    # Puzzle 2
    # What is the sum of the badges for the 3 elf groups

    # Iterate through the rucksacks in groups of 3
    total_group_priorities = 0
    for group in grouper(rucksacks, 3):
        # find the shared items, and use set() to get the unique item
        shared_items = [
            i for i in group[0].items if i in group[1].items and i in group[2].items
        ]
        priorities = [PRIORITIES.find(i) for i in set(shared_items)]
        total_group_priorities += sum(priorities)
        print(f"{shared_items}")
        print(f"Group badge priority is {sum(priorities)}")

    print(f"Sum of group badge priorities is {total_group_priorities}")
