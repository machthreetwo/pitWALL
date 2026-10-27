# Chapter 14 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 14: dunder methods - a Session that behaves like a built-in."""

from functools import total_ordering
from pitwall.display import format_laptime


@total_ordering
class Lap:
    """One timed lap. Ordered by time, so sorted(laps) puts the fastest first."""

    __slots__ = ("driver", "number", "ms")

    def __init__(self, driver: str, number: int, ms: int):
        raise NotImplementedError("Chapter 14: implement __init__")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 14: implement __repr__")

    def __str__(self) -> str:
        raise NotImplementedError("Chapter 14: implement __str__")

    def _key(self) -> tuple:
        raise NotImplementedError("Chapter 14: implement _key")

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("Chapter 14: implement __eq__")

    def __lt__(self, other: "Lap") -> bool:
        raise NotImplementedError("Chapter 14: implement __lt__")

    def __hash__(self) -> int:
        raise NotImplementedError("Chapter 14: implement __hash__")


class Session:
    """A named collection of laps that supports len(), iteration, indexing, `in` and +."""

    def __init__(self, name: str, laps: list[Lap] | None = None):
        raise NotImplementedError("Chapter 14: implement __init__")

    @classmethod
    def from_race(cls, name: str, race: dict[str, list[int]]) -> "Session":
        raise NotImplementedError("Chapter 14: implement from_race")

    def add(self, lap: Lap) -> None:
        raise NotImplementedError("Chapter 14: implement add")

    def __len__(self) -> int:
        raise NotImplementedError("Chapter 14: implement __len__")

    def __iter__(self):
        raise NotImplementedError("Chapter 14: implement __iter__")

    def __getitem__(self, key):
        """session[0] -> a Lap; session[1:3] -> list of Laps; session['VER'] -> that driver's laps."""
        raise NotImplementedError("Chapter 14: implement __getitem__")

    def __contains__(self, driver: str) -> bool:
        raise NotImplementedError("Chapter 14: implement __contains__")

    def __bool__(self) -> bool:
        raise NotImplementedError("Chapter 14: implement __bool__")

    def __add__(self, other: "Session") -> "Session":
        raise NotImplementedError("Chapter 14: implement __add__")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 14: implement __repr__")

    def fastest(self) -> Lap:
        raise NotImplementedError("Chapter 14: implement fastest")

    def drivers(self) -> list[str]:
        raise NotImplementedError("Chapter 14: implement drivers")
