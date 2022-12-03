from typing import Iterable, Iterator, TypeVar

_T = TypeVar("_T")


# From the itertools documentation
def grouper(iterable: Iterable[_T], n: int) -> Iterator[tuple[_T, ...]]:
    """
    Collect data into non-overlapping fixed-length chunks or blocks.
    """
    # grouper('ABCDEFG', 3) --> ABC DEF
    args = [iter(iterable)] * n
    return zip(*args)
