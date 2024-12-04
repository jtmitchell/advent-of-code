from collections.abc import Iterable, Iterator
from itertools import islice, zip_longest
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


def pairwise(iterable: Iterable[_T], n: int) -> Iterator[tuple[_T, ...]]:
    """
    Return a sliding window with n elements, of the iterable.

    s -> (s0,s1,..s(n-1)), (s1,s2,.., sn), (s2, s3,..,s(n+1)), ...
    """
    iters = iter(iterable)
    result = tuple(islice(iters, n))
    if len(result) == n:
        yield result
    for elem in iters:
        result = result[1:] + (elem,)
        yield result
