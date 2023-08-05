from srtlst.collections_abc import Sequence, Callable

from typing import Optional, TypeVar

from srtlst.protocols import _SupportsLT

_T = TypeVar("_T")
_S = TypeVar("_S", bound=_SupportsLT)


def bisect_left(
    seq: Sequence[_T],
    key_value: _S,
    key: Callable[[_T], _S],
    reverse: bool,
    lo: Optional[int] = None,
    hi: Optional[int] = None,
) -> int:
    """
    return the position where an item with key_value should be inserted in
    sorted sequence seq
    if seq already contains items with a key value equal to key_value
    their first position is returned (so that the item would be inserted
    to their left)
    lo and / or  hi may be given to perform the bisection as if called on seq[lo:hi]
    or on seq[lo:] or seq[:hi] if only one of the two is given
    the function key is used to determine the key value for
    each item in the list
    if reverse is true the sequence is considered to be sorted in descending
    order
    """
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(seq)

    if not reverse:
        while lo != hi:
            x = (lo + hi) // 2
            if key(seq[x]) < key_value:
                lo = x + 1
            else:
                hi = x
    else:
        while lo != hi:
            x = (lo + hi) // 2
            if key_value < key(seq[x]):
                lo = x + 1
            else:
                hi = x

    return lo


def bisect_right(
    seq: Sequence[_T],
    key_value: _S,
    key: Callable[[_T], _S],
    reverse: bool,
    lo: Optional[int] = None,
    hi: Optional[int] = None,
) -> int:
    """
    return the position where an item with key_value should be inserted in
    sorted sequence seq
    if seq already contains items with a key value equal to key_value
    their last position plus one is returned (so that the item would be
    inserted to their right)
    lo and / or  hi may be given to perform the bisection as if called on seq[lo:hi]
    or on seq[lo:] or seq[:hi] if only one of the two is given
    the function key is used to determine the key value for
    each item in the list
    if reverse is true the sequence is considered to be sorted in descending
    order
    """
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(seq)

    if not reverse:
        while lo != hi:
            x = (lo + hi) // 2
            if key_value < key(seq[x]):
                hi = x
            else:
                lo = x + 1
    else:
        while lo != hi:
            x = (lo + hi) // 2
            if key(seq[x]) < key_value:
                hi = x
            else:
                lo = x + 1

    return lo
