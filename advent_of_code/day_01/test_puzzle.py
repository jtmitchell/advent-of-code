"""
Unit test for Day 1: Secret Entrance
"""

# ruff: PT006
import pathlib
from pathlib import Path

import pytest

from .puzzle import load_data, solve_pt1, solve_pt2


def test_puzzle_pt1() -> None:
    """
    Run a test against the sample input.
    """
    expected_result = 3
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: int = solve_pt1(data)
    assert result == expected_result


def test_puzzle_pt2_0() -> None:
    """
    Run a test against the sample input.
    """
    # expected_result = 3
    # expected_result = 1
    expected_result = 6
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: int = solve_pt2(data)
    assert result == expected_result


@pytest.mark.parametrize(
    "expected_result, data",  # noqa: PT006
    [
        (3, [("L", 50), ("R", 200)]),
        (1, [("R", 50), ("L", 50)]),
    ],
)
def test_puzzle_pt2_1(expected_result: int, data: list[tuple[str, int]]) -> None:
    """
    Run a test against the sample input.
    """
    result: int = solve_pt2(data)
    assert result == expected_result
