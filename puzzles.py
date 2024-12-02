#!/usr/bin/env python3
import argparse
import importlib


def main():
    """
    Import and run the requested puzzle.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("day")
    parser.add_argument(
        "-2",
        "--part2",
        help="Run the part two puzzle",
        action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args()
    puzzle = importlib.import_module(f"advent_of_code.{args.day}")
    puzzle.run_puzzle(args)


if __name__ == "__main__":
    main()
