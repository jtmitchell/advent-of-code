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

    if args.newrules:
        num_knots = 10
    else:
        num_knots = 2
    knots = [Knot(position=Vector()) for _ in range(num_knots)]
    bridge = Rope(knots=knots, is_test=args.test)

    for direction, steps in movements:
        bridge.move(direction=direction, steps=steps)

    # Puzzle 1
    # How many positions does the tail of the rope visit at least once?
    tail = knots[-1]
    print(
        f"Tail positions {len(tail.all_positions)} and unique {len(tail.unique_positions)}"
    )
    if args.test:
        print(f"Unique tail positions\n{tail.unique_positions}")
        assert (
            len(tail.unique_positions) == 13
        ), f"{len(tail.unique_positions)} is not 13: wrong number of unique positions"

    # Puzzle 2
    # With 10 knots, how many positions does the tail of the rope visit at least once?
