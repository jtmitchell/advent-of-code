import os
import string
import re
from argparse import Namespace

from .models import StackOfCrates
from advent_2022.utils import grouper


def solve(args: Namespace):
    """
    Solve the stacking puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Crates")
    print(f"loading {input_file}")

    MOVEMENT_RE = re.compile(
        r"^move (?P<count>\d+) from (?P<source>\d+) to (?P<destination>\d+)"
    )
    stacks: list[StackOfCrates] = []
    building_stacks = True
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            if building_stacks:
                # print(f"line is {line}")
                for i, group in enumerate(
                    grouper(line, 4, incomplete="fill", fillvalue=" ")
                ):
                    crate = group[1]
                    # print(f"stack {i} crate is {crate}")
                    if "[" in line:
                        if i >= len(stacks):
                            stacks.append(StackOfCrates())
                        if crate in string.ascii_uppercase:
                            stacks[i].crates.insert(0, crate)
                    else:
                        building_stacks = False
            else:
                # Process the movement instructions
                if match := MOVEMENT_RE.search(line):
                    count = int(match.group("count"))
                    source = int(match.group("source"))
                    dest = int(match.group("destination"))
                    # print(f"movement {count=} {source=} {dest=}")
                    if args.newrules:
                        crates = [stacks[source - 1].crates.pop() for _ in range(count)]
                        stacks[dest - 1].crates.extend(reversed(crates))
                    else:
                        for _ in range(count):
                            crate = stacks[source - 1].crates.pop()
                            stacks[dest - 1].crates.append(crate)

    print(f"Read {len(stacks)} assignments")
    for i, stack in enumerate(stacks):
        print(f"Stack {i+1} {stack.crates}")

    # Puzzle 1
    # What crates are on top of the stacks?
    top_of_stacks = [s.crates[-1] for s in stacks]
    print(f"Top of stacks {''.join(top_of_stacks)}")

    # Puzzle 2
    # Same puzzle, using v2 rules for moving
