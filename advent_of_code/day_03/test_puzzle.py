"""
Unit test for Day 3: Lobby
"""

import pathlib
from pathlib import Path

from .puzzle import load_data, solve_pt1, solve_pt2


def test_puzzle_pt1() -> None:
    """
    Run a test against the sample input.
    """
    expected_result: int = 357
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: int = solve_pt1(data)
    assert result == expected_result


def test_puzzle_pt2() -> None:
    """
    Run a test against the sample input.
    """
    expected_result: int = 3121910778619
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: int = solve_pt2(data)
    assert result == expected_result
