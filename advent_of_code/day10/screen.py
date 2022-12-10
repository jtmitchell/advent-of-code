import os
from argparse import Namespace

from advent_of_code.utils import grouper

from .models import CPU, RegisterValue


def solve(args: Namespace):
    """
    Solve the CRT screen puzzle.
    """
    dirname = os.path.dirname(__file__)
    if args.test:
        basefile = "sample2.txt" if args.newrules else "sample.txt"
    else:
        basefile = "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("CRT screen")
    print(f"loading {input_file}")

    cpu = CPU(cycles=[RegisterValue(after=1)])
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            # Each line is a movement instruction
            line = line.strip()
            if " " in line:
                _, value = line.split(" ", maxsplit=1)
                cpu.addx(int(value))
            else:
                cpu.noop()

    # Puzzle 1
    # Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    # What is the sum of these six signal strengths?
    sum_signal_strength = 0
    for cycle in [20, 60, 100, 140, 180, 220]:
        register_value = cpu.cycles[cycle].during
        strength = cycle * register_value
        sum_signal_strength += strength
        print(f"Cycle {cycle} value is {register_value} strength {strength}")
        if args.test:
            expected = {
                20: (21, 420),
                60: (19, 1140),
                100: (18, 1800),
                140: (21, 2940),
                180: (16, 2880),
                220: (18, 3960),
            }
            assert (
                register_value == expected[cycle][0]
            ), f"Cycle {cycle} wrong register value {register_value}"
            assert (
                strength == expected[cycle][1]
            ), f"Cycle {cycle} wrong strength value {strength}"

    if args.test:
        assert (
            sum_signal_strength == 13140
        ), f"Wrong sum of signal strengths {sum_signal_strength}"
    print(f"Sum of signal strength is {sum_signal_strength}")

    # Puzzle 2
    # Render the image given by your program. What eight capital letters appear on your CRT?
    crt = []
    for cycle, register in enumerate(cpu.cycles):
        position = cycle % 40
        pixel = [register.after - 1, register.after, register.after + 1]
        if position in pixel:
            crt.append("#")
        else:
            crt.append(".")

    for row in grouper(crt, 40, incomplete="fill", fillvalue="."):
        print("".join(row))
