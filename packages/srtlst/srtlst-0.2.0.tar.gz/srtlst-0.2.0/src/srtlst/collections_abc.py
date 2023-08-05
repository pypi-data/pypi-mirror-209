from sys import version_info

if version_info >= (3, 9):
    from collections.abc import (
        Callable,
        Collection,
        Container,
        Iterable,
        Reversible,
        Sequence,
        Sized,
    )
else:
    from typing import (
        Callable,
        Collection,
        Container,
        Iterable,
        Reversible,
        Sequence,
        Sized,
    )

__all__ = [
    "Callable",
    "Collection",
    "Container",
    "Iterable",
    "Reversible",
    "Sequence",
    "Sized",
]
