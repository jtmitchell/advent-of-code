import os
from argparse import Namespace
from .models import Rope, Knot, Vector


def solve(args: Namespace):
    """
    Solve the rope bridge puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Rope bridge")
    print(f"loading {input_file}")

    movements = []
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            # Each line is a movement instruction
            line = line.strip()
            direction, distance = line.split(" ", maxsplit=1)
            steps = int(distance)
            movements.append((direction, steps))

    head = Knot(position=Vector())
    tail = Knot(position=Vector())
    bridge = Rope(head=head, tail=tail, is_test=args.test)

    for direction, steps in movements:
        bridge.move(direction=direction, steps=steps)

    # Puzzle 1
    # How many positions does the tail of the rope visit at least once?

    # Puzzle 2
