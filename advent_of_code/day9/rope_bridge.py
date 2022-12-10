import os
from argparse import Namespace
from .models import Rope, Knot, Vector


def solve(args: Namespace):
    """
    Solve the rope bridge puzzle.
    """
    dirname = os.path.dirname(__file__)
    if args.test:
        basefile = "sample2.txt" if args.newrules else "sample.txt"
    else:
        basefile = "input.txt"
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

    bridge = Rope(
        knots=[Knot(position=Vector()) for _ in range(num_knots)], is_test=args.test
    )

    for direction, steps in movements:
        bridge.move(direction=direction, steps=steps)

    # Puzzle 1
    # How many positions does the tail of the rope visit at least once?
    tail = bridge.tail
    print(
        f"Tail positions {len(tail.all_positions)} and unique {len(tail.unique_positions)}"
    )
    if args.test:
        print(f"Unique tail positions\n{tail.unique_positions}")
        if args.newrules:
            expected_value = 36
        else:
            expected_value = 13
        assert len(tail.unique_positions) == expected_value, (
            f"{len(tail.unique_positions)} is not {expected_value}: "
            f"wrong number of unique positions"
        )

    # Puzzle 2
    # With 10 knots, how many positions does the tail of the rope visit at least once?
