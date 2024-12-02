"""
Unit test for puzzles.

Advent of Code Puzzle.
Day 1: Historian Hysteria
"""

import os

from .puzzle import load_data, solve


def test_puzzle():
    """
    Run a test against the sample input.
    """
    expected_result = None
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt"
    input_file = os.path.join(dirname, basefile)

    data = load_data(input_file)
    result = solve(data)
    assert result == expected_result
