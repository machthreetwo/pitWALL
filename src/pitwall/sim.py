# Chapter 4 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 4: functions - the simulate_lap() family."""

import random

DEFAULT_GRID: dict[str, int] = {
    "Max Verstappen": 90100,
    "Lando Norris": 90000,
    "Charles Leclerc": 90250,
    "Oscar Piastri": 90150,
    "Lewis Hamilton": 90400,
    "George Russell": 90350,
}


def simulate_lap(
    base_ms: int,
    tyre_age: int,
    *,
    deg_ms: int = 80,
    fuel_kg: float = 0.0,
    kg_effect_ms: int = 30,
    noise_ms: float = 0.0,
    rng: random.Random | None = None,
) -> int:
    """One lap: base + tyre degradation + fuel weight + random noise.

    Keyword-only arguments (after *) cannot be passed by position, so a call
    reads like a spec: simulate_lap(90_000, 5, deg_ms=60).
    """
    raise NotImplementedError("Chapter 4: implement simulate_lap")


def simulate_stint(
    base_ms: int,
    laps: int,
    start_age: int = 0,
    fuel_start_kg: float = 0.0,
    burn_kg_per_lap: float = 0.0,
    **lap_kwargs,
) -> list[int]:
    """Run consecutive laps on one set of tyres. Extra kwargs go straight to simulate_lap."""
    raise NotImplementedError("Chapter 4: implement simulate_stint")


def simulate_race(
    drivers: dict[str, int], laps: int, *, seed: int | None = None, **lap_kwargs
) -> dict[str, list[int]]:
    """Simulate every driver over the same distance with one shared, seeded RNG."""
    raise NotImplementedError("Chapter 4: implement simulate_race")


def best_of(*laptimes: int) -> int:
    """Fastest of any number of lap times passed as separate arguments."""
    raise NotImplementedError("Chapter 4: implement best_of")


def log_lap(lap_ms: int, log: list[int] | None = None) -> list[int]:
    """Append to a log, creating a fresh one when none is given.

    The tempting signature `log=[]` shares ONE list across every call.
    """
    raise NotImplementedError("Chapter 4: implement log_lap")
