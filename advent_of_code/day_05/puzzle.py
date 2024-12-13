"""
Advent of Code Puzzle.
Day 5: Print Queue
"""

import pathlib
from argparse import Namespace
from dataclasses import dataclass, field


@dataclass
class PageLookup:
    after: list[int] = field(default_factory=list)
    before: list[int] = field(default_factory=list)


def run_puzzle(args: Namespace):
    """
    Run the puzzle.
    """

    input_file = pathlib.Path(__file__).with_name("input.txt")
    data = load_data(input_file)

    # Print the solution
    result = solve_pt1(data) if not args.part2 else solve_pt2(data)
    print(f"Result is {result}")


def load_data(datafile: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
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


def check_ordering(page_ordering: list[tuple[int, int]], pages: list[int]) -> bool:
    """
    Check the page ordering.
    """
    for first_page, second_page in page_ordering:
        if first_page not in pages or second_page not in pages:
            continue
        if pages.index(first_page) > pages.index(second_page):
            return False
    return True


def fix_order(page_ordering: list[tuple[int, int]], pages: list[int]) -> list[int]:  # noqa: C901
    """
    Fix the ordering of the incorrect pages.
    """
    filtered_order = [(x, y) for x, y in page_ordering if x in pages and y in pages]
    lookup = {}
    for first_page, second_page in filtered_order:
        p1 = lookup.get(first_page, PageLookup())
        p1.before.append(second_page)
        lookup[first_page] = p1

        p2 = lookup.get(second_page, PageLookup())
        p2.after.append(first_page)
        lookup[second_page] = p2

    fixed_pages = []
    for first_page, second_page in filtered_order:
        if first_page not in fixed_pages:
            fixed_pages.insert(0, first_page)
        else:
            fixed_pages.pop(fixed_pages.index(first_page))
            idx_before = [
                fixed_pages.index(x) for x in lookup[first_page].before if x in fixed_pages
            ]
            idx_after = [
                fixed_pages.index(x) for x in lookup[first_page].after if x in fixed_pages
            ]
            idx_before = min(idx_before) if idx_before else None
            idx_after = max(idx_after) if idx_after else None
            if idx_before is not None and idx_after is not None:
                if idx_before > idx_after:
                    fixed_pages.insert(idx_before, first_page)
                else:
                    fixed_pages.insert(idx_after, first_page)
            elif idx_before is not None:
                fixed_pages.insert(idx_before, first_page)
            elif idx_after is not None:
                fixed_pages.insert(idx_after, first_page)

        if second_page not in fixed_pages:
            fixed_pages.append(second_page)
        else:
            fixed_pages.pop(fixed_pages.index(second_page))
            idx_before = [
                fixed_pages.index(x) for x in lookup[second_page].before if x in fixed_pages
            ]
            idx_after = [
                fixed_pages.index(x) for x in lookup[second_page].after if x in fixed_pages
            ]
            idx_before = min(idx_before) if idx_before else None
            idx_after = max(idx_after) if idx_after else None
            if idx_before is not None and idx_after is not None:
                if idx_before > idx_after:
                    fixed_pages.insert(idx_before, second_page)
                else:
                    fixed_pages.insert(idx_after, second_page)
            elif idx_before is not None:
                fixed_pages.insert(idx_before, second_page)
            elif idx_after is not None:
                fixed_pages.insert(idx_after, second_page)

    return fixed_pages


def solve_pt1(data: tuple[list[tuple[int, int]], list[list[int]]]):
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


def solve_pt2(data: tuple[list[tuple[int, int]], list[list[int]]]):
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
