set dotenv-load := true

# This list of available targets
default:
    @just --list

# Make virtual environment
venv:
    uv venv --python python3.12

# Install python DEV dependancies
install:
    uv sync
    uv run pre-commit install --hook-type pre-commit

# Create a new day
new_day:
    uv run cookiecutter templates/ --output-dir advent_of_code/

# Run pytest
test day="":
    uv run pytest advent_of_code/{{day}}

# Run a puzzle
puzzle +options="":
    uv run ./puzzles.py {{options}}
