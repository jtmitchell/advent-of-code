# Advent of Code

Code to solve the [Advent of Code](https://adventofcode.com/) puzzles.

The current year's puzzles are in the main branch, and any previous years are in branches.

## Puzzles

* [Advent of Code 2024](./advent_of_code/README.md)

### Cookiecutter

There is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create the bare code for a new day's puzzle.

To start a new puzzle, run ``just new_day``, and fill in the prompts.

## Install

Use the [``justfile``](https://github.com/casey/just) command to install everything, using [``uv``](https://github.com/astral-sh/uv).
```
just install
```

### Python

* Install [``uv``](https://github.com/astral-sh/uv) as the package manager.
* Run ``uv sync`` to install the dependancies.


### Pre-Commit

The project is using [``pre-commit``](https://pre-commit.com/) to do some checking when commiting.

If you did not use the ``just install`` command, then manually install the commit hooks with
```
uv run pre-commit install --hook-type pre-commit
```

The ``pre-commit`` checks will run when you commit code,
and may stop you committing the code until the checks are passing.

* To run the checks on the changed files, before the commit, run ``pre-commit run``
* To run the checks on all the files, run ``pre-commit run --all-files``
