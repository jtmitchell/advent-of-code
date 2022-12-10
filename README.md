# Advent of Code
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://gitlab.com/jtmitchell/advent-of-code)

Code to solve the [Advent of Code](https://adventofcode.com/) puzzles.

## Puzzles

* [Advent of Code 2022](./advent_of_code/README.md)


## Install

### Pre-Commit

The project is using ``pre-commit`` to do some checking when commiting.

* install the [pre-commit hooks for git](https://pre-commit.com/)
```
pre-commit install --hook-type pre-commit
```

The pre-commit hooks are configured to do the following:
* format the code using [**black**](https://github.com/psf/black)
* run flake8 to check the code
* fix trailing whitespace
* validate yaml files
* check we are not adding huge files to the repo

The ``pre-commit`` checks will run when you commit code,
and may stop you committing the code until the checks are passing.

* To run the checks on the changed files, before the commit, run ``pre-commit run``
* To run the checks on all the files, run ``pre-commit run --all-files``
