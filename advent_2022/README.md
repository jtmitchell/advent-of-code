# Advent of Code 2022

Code to solve the [2022 Advent of Code](https://adventofcode.com/2022) puzzles.

## Puzzles

* [Day 1: Calorie Counting](./day1/README.md)
* [Day 2: Rock Paper Scissors](./day2/README.md)
* [Day 3: Rucksack Reorganization](./day3/README.md)
* [Day 4: Camp Cleanup](./day4/README.md)
* [Day 5: Supply Stacks](./day5/README.md)
* [Day 6: Tuning Trouble](./day6/README.md)
* [Day 7: No Space Left On Device](./day7/README.md)


## Install

### Python

Create a virtual environment, and install the Python dependancies.
* setup a Python virtual enviroment
* install the development dependancies
```
pip install -r requirements.txt
```

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
