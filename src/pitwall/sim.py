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
    """• Everything after tyre_age must be keyword-only (a * in the signature).
simulate_lap(90_000, 5, 60) must raise TypeError .
• If noise_ms is non-zero, add rng.gauss(0, noise_ms) . If rng is None , create a new
random.Random() .
• If noise_ms is 0, do not draw any random number.
• The same seeded rng must give the same result: simulate_lap(90_000, 0, noise_ms=200,
rng=random.Random(1)) is identical every time."""
 
    lap=base_ms+deg_ms*tyre_age+fuel_kg*kg_effect_ms
    if noise_ms: #checks truthliness if noise_ms is really not 0
        rng=rng or random.Random()
        lap+=rng.gauss(0,noise_ms)
    return round(lap)



def simulate_stint(
    base_ms: int,
    laps: int,
    start_age: int = 0,
    fuel_start_kg: float = 0.0,
    burn_kg_per_lap: float = 0.0,
    **lap_kwargs,
) -> list[int]:
    """Run consecutive laps on one set of tyres. Extra kwargs go straight to simulate_lap."""
    times=[]
    fuel=fuel_start_kg
    for i in range(laps):
        times.append(simulate_lap(base_ms,start_age+i,fuel_kg=fuel,**lap_kwargs))
        fuel=max(0.0, fuel-burn_kg_per_lap)
    return times



def simulate_race(
    drivers: dict[str, int], laps: int, *, seed: int | None = None, **lap_kwargs
) -> dict[str, list[int]]:
    """Simulate every driver over the same distance with one shared, seeded RNG."""
    rng=random.Random(seed)
    return {
        name: simulate_stint(base,laps,rng=rng,**lap_kwargs)
        for name,base in drivers.items()
    }


def best_of(*laptimes: int) -> int:
    """Fastest of any number of lap times passed as separate arguments."""
    if not laptimes:
        raise ValueError("at least one lap time is required")
    return min(laptimes)


def log_lap(lap_ms: int, log: list[int] | None = None) -> list[int]:
    """Append to a log, creating a fresh one when none is given.

    The tempting signature `log=[]` shares ONE list across every call.
    """
    if log is None:
        log=[]
    log.append(lap_ms)
    return log
