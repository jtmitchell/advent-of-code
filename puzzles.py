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
        "-t",
        "--test",
        help="Run against the test data",
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "-2",
        "--newrules",
        help="Run using V2 of the rules",
        action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args()
    puzzle = importlib.import_module(f"advent_of_code.{args.day}")
    puzzle.run_puzzle(args)


if __name__ == "__main__":
    main()
