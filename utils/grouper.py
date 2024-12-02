from collections.abc import Iterable, Iterator
from itertools import zip_longest
from typing import TypeVar

_T = TypeVar("_T")


def grouper(
    iterable: Iterable[_T], n: int, *, incomplete: str = "ignore", fillvalue=None
) -> Iterator[tuple[_T, ...]]:
    """
    Collect data into non-overlapping fixed-length chunks or blocks.
    """
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args, strict=False)

    raise ValueError("Expected fill, strict, or ignore")
