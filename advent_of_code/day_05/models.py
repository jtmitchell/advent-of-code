"""
Models for Day 5: Cafeteria.
"""

from dataclasses import dataclass


@dataclass
class FruitIdRange:
    start: int = 0
    stop: int = 0


class FreshFruit:
    fresh_ids: list[FruitIdRange | None] = None

    def __init__(self) -> None:
        self.fresh_ids = []

    def add_range(self, range=tuple[int, int]) -> None:
        start, stop = sorted(range)
        self.fresh_ids.append(FruitIdRange(start=start, stop=stop))

    def is_fresh(self, id: int) -> bool:
        for r in self.fresh_ids:
            if r.start <= id <= r.stop:
                return True

        return False

    def fresh_stock_count(self) -> int:
        ranges: list[FruitIdRange] = []
        # Loop through all the fresh ranges
        # Sort the fields by start, so we can extend the ranges correctly
        for i in sorted(self.fresh_ids, key=lambda x: x.start):
            # Loop through all the combined ranges found so far
            save_range = True
            for r in ranges:
                is_inside_range = all(
                    [r.start <= i.start < r.stop, r.start <= i.stop <= r.stop]
                )
                # If the range is entirely inside another range, we can skip it.
                if is_inside_range:
                    save_range = False
                    break

                # There is an overlap, so extend the start of end to make one inside the other
                if i.start <= r.start <= i.stop <= r.stop:
                    r.start = i.start
                    save_range = False
                elif r.start <= i.start <= r.stop <= i.stop:
                    r.stop = i.stop
                    save_range = False
                else:
                    continue

            if save_range:
                ranges.append(i)

        counters = [len(range(i.start, i.stop)) for i in ranges]
        return sum(counters)
