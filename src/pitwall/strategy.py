# Chapter 13 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 13: inheritance, composition and abstract base classes - strategies."""

from abc import ABC, abstractmethod

PIT_LOSS_MS = 22000
CLIFF_PENALTY_MS = 1500


class Compound(ABC):
    """What every tyre compound must define. You cannot instantiate this directly."""

    name: str = "abstract"

    @property
    @abstractmethod
    def pace_offset_ms(self) -> int: ...

    @property
    @abstractmethod
    def deg_ms(self) -> int: ...

    @property
    @abstractmethod
    def life(self) -> int: ...

    def lap_penalty(self, age: int) -> int:
        """Time lost vs a perfect tyre on a lap at this age (shared by every subclass)."""
        raise NotImplementedError("Chapter 13: implement lap_penalty")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 13: implement __repr__")


class Soft(Compound):
    name = "soft"
    pace_offset_ms = 0
    deg_ms = 110
    life = 18


class Medium(Compound):
    name = "medium"
    pace_offset_ms = 350
    deg_ms = 75
    life = 28


class Hard(Compound):
    name = "hard"
    pace_offset_ms = 700
    deg_ms = 50
    life = 40


COMPOUNDS: dict[str, type[Compound]] = {cls.name: cls for cls in (Soft, Medium, Hard)}


def compound_from_name(name: str) -> Compound:
    raise NotImplementedError("Chapter 13: implement compound_from_name")


class Strategy(ABC):
    """A plan: an ordered list of (compound, laps) stints covering the race."""

    @abstractmethod
    def stints(self, total_laps: int) -> list[tuple[Compound, int]]: ...

    def pit_laps(self, total_laps: int) -> list[int]:
        """Lap numbers on which the car pits (end of every stint but the last)."""
        raise NotImplementedError("Chapter 13: implement pit_laps")

    def estimate_race_ms(self, base_ms: int, total_laps: int) -> int:
        raise NotImplementedError("Chapter 13: implement estimate_race_ms")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 13: implement __repr__")


class OneStop(Strategy):
    def __init__(self, first: Compound, second: Compound, pit_lap: int):
        raise NotImplementedError("Chapter 13: implement __init__")

    def stints(self, total_laps: int) -> list[tuple[Compound, int]]:
        raise NotImplementedError("Chapter 13: implement stints")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 13: implement __repr__")


class TwoStop(Strategy):
    def __init__(self, compounds: tuple[Compound, Compound, Compound], pit_laps: tuple[int, int]):
        raise NotImplementedError("Chapter 13: implement __init__")

    def stints(self, total_laps: int) -> list[tuple[Compound, int]]:
        raise NotImplementedError("Chapter 13: implement stints")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 13: implement __repr__")


def best_strategy(strategies: list[Strategy], base_ms: int, total_laps: int) -> Strategy:
    """Polymorphism: each strategy answers estimate_race_ms() its own way."""
    raise NotImplementedError("Chapter 13: implement best_strategy")
