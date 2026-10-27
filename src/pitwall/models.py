# Chapter 12 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 12: classes - Tyre, Driver and Car."""

import random
from pitwall.display import driver_code
from pitwall.sim import simulate_lap


class Tyre:
    """A set of tyres that ages one lap at a time."""

    LIFE = {"soft": 18, "medium": 28, "hard": 40}
    DEG_MS = {"soft": 110, "medium": 75, "hard": 50}

    def __init__(self, compound: str, age: int = 0):
        raise NotImplementedError("Chapter 12: implement __init__")

    @staticmethod
    def is_valid(compound: str) -> bool:
        raise NotImplementedError("Chapter 12: implement is_valid")

    @classmethod
    def used(cls, compound: str, age: int) -> "Tyre":
        """Alternative constructor for a scrubbed set."""
        raise NotImplementedError("Chapter 12: implement used")

    @property
    def wear(self) -> float:
        """Fraction of life used (can exceed 1.0 past the cliff)."""
        raise NotImplementedError("Chapter 12: implement wear")

    @property
    def deg_ms(self) -> int:
        raise NotImplementedError("Chapter 12: implement deg_ms")

    def is_past_cliff(self) -> bool:
        raise NotImplementedError("Chapter 12: implement is_past_cliff")

    def run_lap(self) -> None:
        raise NotImplementedError("Chapter 12: implement run_lap")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 12: implement __repr__")


class Driver:
    def __init__(self, name: str, base_ms: int):
        raise NotImplementedError("Chapter 12: implement __init__")

    @property
    def code(self) -> str:
        raise NotImplementedError("Chapter 12: implement code")

    def __repr__(self) -> str:
        raise NotImplementedError("Chapter 12: implement __repr__")


class Car:
    """A driver + current tyres + fuel. Composition: a Car HAS a Driver and a Tyre."""

    BURN_KG_PER_LAP = 1.6

    def __init__(self, driver: Driver, tyre: Tyre, fuel_kg: float = 100.0):
        raise NotImplementedError("Chapter 12: implement __init__")

    def drive_lap(self, noise_ms: float = 0.0, rng: random.Random | None = None) -> int:
        """Simulate one lap, then age the tyre and burn fuel. Returns the lap time."""
        raise NotImplementedError("Chapter 12: implement drive_lap")

    def pit(self, compound: str, loss_ms: int = 22000) -> None:
        """Fit fresh tyres. The time lost is added to the most recent lap."""
        raise NotImplementedError("Chapter 12: implement pit")

    @property
    def total_ms(self) -> int:
        raise NotImplementedError("Chapter 12: implement total_ms")
