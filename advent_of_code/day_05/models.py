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
