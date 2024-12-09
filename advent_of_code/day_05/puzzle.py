"""
Advent of Code Puzzle.
Day 5: Print Queue
"""

import pathlib
from argparse import Namespace


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> tuple[tuple[int, int], list[list[int]]]:
    """
    Load the puzzle data.
    """
    pages_list = []
    page_ordering = []

    print(f"loading {datafile}")
    with open(datafile, encoding="utf8") as fh:
        for line in fh:
            if "|" in line:
                first_page, second_page = line.split("|", maxsplit=1)
                page_ordering.append((int(first_page.strip()), int(second_page.strip())))
            elif "," in line:
                pages_list.append([int(p.strip()) for p in line.split(",")])

    return page_ordering, pages_list


def check_ordering(page_ordering: tuple[int, int], pages: list[int]) -> bool:
    """
    Check the page ordering.
    """
    for first_page, second_page in page_ordering:
        if first_page not in pages or second_page not in pages:
            continue
        if pages.index(first_page) > pages.index(second_page):
            return False
    return True


def fix_order(page_ordering: tuple[int, int], pages: list[int]) -> list[int]:
    """
    Fix the ordering of the incorrect pages.
    """
    return pages


def solve_pt1(data: tuple[tuple[int, int], list[int]]):
    """
    Solve the part one puzzle.
    """
    page_ordering, pages_list = data
    valid_pages = [
        pages
        for pages in pages_list
        if check_ordering(page_ordering=page_ordering, pages=pages)
    ]

    mid_pages = [pages[int(abs(len(pages) / 2))] for pages in valid_pages]
    return sum(mid_pages)


def solve_pt2(data: tuple[tuple[int, int], list[int]]):
    """
    Solve the part two puzzle.
    """
    page_ordering, pages_list = data
    invalid_pages = [
        pages
        for pages in pages_list
        if not check_ordering(page_ordering=page_ordering, pages=pages)
    ]
    fixed_pages = [
        fix_order(page_ordering=page_ordering, pages=pages) for pages in invalid_pages
    ]

    mid_pages = [pages[int(abs(len(pages) / 2))] for pages in fixed_pages]
    return sum(mid_pages)
