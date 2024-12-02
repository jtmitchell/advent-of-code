"""
Unit test for Day {{cookiecutter.day_number}}: {{cookiecutter.puzzle_name}}
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
