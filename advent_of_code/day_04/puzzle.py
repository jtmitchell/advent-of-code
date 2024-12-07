"""
Advent of Code Puzzle.
Day 4: Ceres Search
"""

import pathlib
from argparse import Namespace

from utils.vector import Vector


def adjacent(loc_a: Vector, loc_b: Vector) -> bool:
    """
    Return true is the locations are next to each other.
    """
    path = loc_a - loc_b
    return True if all([0 <= abs(path.x) <= 1, 0 <= abs(path.y) <= 1]) else False


def direction_to(loc_a: Vector, loc_b: Vector) -> Vector:
    """
    Return a direction vector from this location to the next.
    """
    path = loc_a - loc_b
    if path.x < 0:
        path.x = -1
    elif path.x > 0:
        path.x = 1
    if path.y < 0:
        path.y = -1
    elif path.y > 0:
        path.y = 1

    return path


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> dict[str, list[Vector]]:
    """
    Load the puzzle data.
    """
    print(f"loading {datafile}")
    data = dict(x=[], m=[], a=[], s=[])
    with open(datafile, encoding="utf8") as fh:
        for row, line in enumerate(fh):
            for col, letter in enumerate(line):
                if letter.lower() in "xmas":
                    data[letter.lower()].append(Vector(x=row, y=col))
    return data


def solve_pt1(data: dict[str, list[Vector]]):
    """
    Solve the part one puzzle.
    """
    solutions = []

    # Loop through the letters in XMAS.
    # Find each possible variation where the letters are next to each other
    # either horizontally, vertically, or diagonally.
    # Only keep those that move in the same direction.
    for loc_x in data["x"]:
        for loc_m in [i for i in data["m"] if adjacent(i, loc_x)]:
            direction = loc_x - loc_m
            for loc_a in [i for i in data["a"] if adjacent(i, loc_m)]:
                if loc_m - loc_a != direction:
                    continue
                for loc_s in [i for i in data["s"] if adjacent(i, loc_a)]:
                    if loc_a - loc_s != direction:
                        continue
                    solutions.append([loc_x, loc_m, loc_a, loc_s])

    return len(solutions)


def solve_pt2(data: dict[str, list[Vector]]):
    """
    Solve the part two puzzle.
    """
    # This holds a list of directions for each cross point "A"
    solutions = {}

    # Loop through the letters in MAS.
    # Find each possible variation where the letters are next to each other diagonally.
    # Only keep those that move in the same direction.
    # Determine how many solutions cross on the "A"
    for loc_m in data["m"]:
        for loc_a in [i for i in data["a"] if adjacent(i, loc_m)]:
            direction = loc_m - loc_a
            if any([direction.x == 0, direction.y == 0]):
                # Ignore any words that are not on a diagonal
                continue
            for loc_s in [i for i in data["s"] if adjacent(i, loc_a)]:
                if loc_a - loc_s != direction:
                    continue
                direction_list = solutions.get(loc_a, [])
                direction_list.append(direction)
                solutions[loc_a] = direction_list

    # Count the number of cross points with two directions
    return len([k for k, v in solutions.items() if len(v) == 2])
