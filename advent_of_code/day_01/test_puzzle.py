"""
Unit test for puzzles.

Advent of Code Puzzle.
Day 1: Historian Hysteria
"""

import pathlib

from .puzzle import load_data, solve_pt1, solve_pt2


def test_puzzle_pt1():
    """
    Run a test against the sample input.
    """
    expected_result = 11
    input_file = pathlib.Path(__file__).with_name("sample.txt")

    data = load_data(input_file)
    result = solve_pt1(data)
    assert result == expected_result


def test_puzzle_pt2():
    """
    Run a test against the sample input.
    """
    expected_result = 31
    input_file = pathlib.Path(__file__).with_name("sample.txt")

    data = load_data(input_file)
    result = solve_pt2(data)
    assert result == expected_result
