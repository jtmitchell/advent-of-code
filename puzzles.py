#!/usr/bin/env python3
import argparse
import importlib
from argparse import ArgumentParser, Namespace
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


def main() -> None:
    """
    Import and run the requested puzzle.
    """
    parser: ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("day")
    parser.add_argument(
        "-2",
        "--part2",
        help="Run the part two puzzle",
        action=argparse.BooleanOptionalAction,
    )
    args: Namespace = parser.parse_args()
    puzzle: ModuleType = importlib.import_module(name=f"advent_of_code.{args.day}")
    puzzle.run_puzzle(args)


if __name__ == "__main__":
    main()
