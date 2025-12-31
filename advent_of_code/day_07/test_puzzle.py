"""
Unit test for Day 7: Laboratories
"""

import pathlib
from contextlib import nullcontext
from pathlib import Path

import pytest

from .puzzle import load_data, solve_pt1, solve_pt2


@pytest.mark.parametrize(
    "expected_result, filename, num_lines",  # noqa: PT006
    [
        (1, "sample.txt", 2),
        (3, "sample.txt", 3),
        (3, "sample.txt", 4),
        (21, "sample.txt", None),
    ],
)
def test_puzzle_pt1(expected_result, filename, num_lines) -> None:
    """
    Run a test against the sample input.
    """
    input_file: Path = pathlib.Path(__file__).with_name(name=filename)

    data = load_data(datafile=input_file)

    if num_lines is not None:
        data = list(data)[:num_lines]

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
