"""
Unit test for Day {{cookiecutter.day_number}}: {{cookiecutter.puzzle_name}}
"""

import pathlib
from pathlib import Path

from .puzzle import load_data, solve_pt1, solve_pt2


def test_puzzle_pt1() -> None:
    """
    Run a test against the sample input.
    """
    expected_result = {{cookiecutter.expected_test_result}}
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: bool = solve_pt1(data)
    assert result == expected_result


def test_puzzle_pt2() -> None:
    """
    Run a test against the sample input.
    """
    expected_result = None
    input_file: Path = pathlib.Path(__file__).with_name(name="sample.txt")

    data = load_data(datafile=input_file)
    result: bool = solve_pt2(data)
    assert result == expected_result
