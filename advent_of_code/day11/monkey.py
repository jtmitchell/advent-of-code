import os
import re
import math
from argparse import Namespace

from .models import Monkey, Troop


def solve(args: Namespace):
    """
    Solve the monkey puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Monkey business")
    print(f"loading {input_file}")

    with open(input_file, "r", encoding="utf8") as fh:
        data = fh.read()

    monkey_re = (
        r"Monkey (?P<id>\d+?):"
        r"\s+?Starting items: (?P<items>[\d\s,]+?)"
        r"\s+?Operation: new = old (?P<op>[*+]) (?P<op_value>.+?)"
        r"\s+?Test: divisible by (?P<divisor>\d+?)"
        r"\s+?If true: throw to monkey (?P<monkey_true>\d+)"
        r"\s+?If false: throw to monkey (?P<monkey_false>\d+)"
    )

    if args.newrules:
        relief = None
    else:
        relief = 3

    troop = Troop()
    for m in re.finditer(monkey_re, data):
        print(f"Match {m}")
        s_items = m.group("items").split(",")
        items = [int(i.strip()) for i in s_items]
        monkey = Monkey(
            id=int(m.group("id")),
            items=items,
            monkey_true=int(m.group("monkey_true")),
            monkey_false=int(m.group("monkey_false")),
            test_divisible=int(m.group("divisor")),
            operation=(m.group("op"), m.group("op_value")),
            relief=relief,
        )
        # The monkey id should also happen to be the index list
        assert monkey.id == len(troop.monkeys)
        troop.monkeys.append(monkey)

    print(f"All the monkeys\n{troop.monkeys}")

    # Puzzle 1
    # What is the level of monkey business after 20 rounds of
    # stuff-slinging simian shenanigans?

    # Puzzle 2
    # Worry levels are no longer divided by three after each item is inspected;
    # you'll need to find another way to keep your worry levels manageable.
    # Starting again from the initial state in your puzzle input,
    # what is the level of monkey business after 10000 rounds?

    if args.newrules:
        rounds = 10000
    else:
        rounds = 20

    for i in range(rounds):
        troop.monkey_business()
        if args.test:
            if not args.newrules or i in [1, 20, 1000, 10000]:
                print(f"Round {i}")
                troop.show_hands()

    monkey_business = [(m.id, m.total_inspections) for m in troop.monkeys]
    monkey_business = sorted(monkey_business, key=lambda x: x[1])
    print(f"All the monkey business {monkey_business}")
    print(f"Top 2 monkey business {monkey_business[-2:]}")

    total_monkey_business = math.prod([x[1] for x in monkey_business[-2:]])
    print(f"Total monkey business is {total_monkey_business}")

    if args.test:
        if args.newrules:
            assert total_monkey_business == 2713310158
        else:
            assert total_monkey_business == 10605
