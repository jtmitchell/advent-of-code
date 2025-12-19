"""
Unit test for Day 7: Laboratories
"""

import pathlib
from contextlib import nullcontext
from pathlib import Path

import pytest

from .puzzle import load_data, solve_pt1, solve_pt2


@pytest.mark.parametrize(
    "expected_result, filename",  # noqa: PT006
    [
        (21, "sample.txt"),
    ],
)
def test_puzzle_pt1(expected_result, filename) -> None:
    """
    Run a test against the sample input.
    """
    input_file: Path = pathlib.Path(__file__).with_name(name=filename)

    data = load_data(datafile=input_file)

    context = pytest.raises(NotImplementedError) if expected_result is None else nullcontext()
    with context:
        result: int = solve_pt1(data)

    if expected_result:
        assert result == expected_result


@pytest.mark.parametrize(
    "expected_result, filename",  # noqa: PT006
    [
        (None, "sample.txt"),
    ],
)
def test_puzzle_pt2(expected_result, filename) -> None:
    """
    Run a test against the sample input.
    """
    input_file: Path = pathlib.Path(__file__).with_name(name=filename)

    data = load_data(datafile=input_file)

    context = pytest.raises(NotImplementedError) if expected_result is None else nullcontext()
    with context:
        result: int = solve_pt2(data)

    if expected_result:
        assert result == expected_result
