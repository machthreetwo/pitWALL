# Chapter 16 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 16: iterators and generators - a streaming live-telemetry feed."""

import math
import random
from collections.abc import Iterable, Iterator
from pitwall.telemetry import Sample


class LapClock:
    """A hand-written iterator: yields lap numbers 1..total, then stops.

    This is what a generator does for you automatically.
    """

    def __init__(self, total_laps: int):
        raise NotImplementedError("Chapter 16: implement __init__")

    def __iter__(self) -> "LapClock":
        raise NotImplementedError("Chapter 16: implement __iter__")

    def __next__(self) -> int:
        raise NotImplementedError("Chapter 16: implement __next__")


def telemetry_stream(n_samples: int, *, hz: int = 10, seed: int | None = None) -> Iterator[Sample]:
    """Lazily generate samples of a car going round a lap with 4 braking zones.

    Nothing is computed until someone asks for the next sample. For sample i:
        t_ms     = i * (1000 // hz)
        phase    = (i % 200) / 200 * 2*pi           (a lap is 200 samples)
        wave     = sin(4 * phase)                   (4 straights + 4 corners)
        braking  = wave < -0.6
        speed    = max(60.0, 220 + 100*wave + rng.gauss(0, 3)), rounded to 1 dp
        throttle = 0.0 if braking else min(1.0, 0.55 + 0.5*(wave + 1)/2), rounded to 2 dp
        gear     = clamp(int(speed // 40), 1, 8)
    Use random.Random(seed) for the noise.
    """
    raise NotImplementedError("Chapter 16: implement telemetry_stream")


def take(n: int, iterable: Iterable) -> Iterator:
    """First n items of any iterable, lazily. Works on infinite streams."""
    raise NotImplementedError("Chapter 16: implement take")


def rolling_mean(values: Iterable[float], window: int) -> Iterator[float]:
    """Mean of the last `window` values, emitted once the window is full."""
    raise NotImplementedError("Chapter 16: implement rolling_mean")


def braking_zones(samples: Iterable[Sample]) -> Iterator[tuple[int, int]]:
    """(start_t_ms, end_t_ms) of each run of consecutive braking samples."""
    raise NotImplementedError("Chapter 16: implement braking_zones")


def speeds(samples: Iterable[Sample]) -> Iterator[float]:
    """Pipeline stage: Sample stream -> speed stream (a generator expression)."""
    raise NotImplementedError("Chapter 16: implement speeds")
