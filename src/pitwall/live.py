# Chapter 21 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 21: concurrency - threads, processes and asyncio."""

import asyncio
import random
import threading
from collections.abc import AsyncIterator
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


async def car_feed(
    code: str, laps: int, *, delay_s: float = 0.0, seed: int = 0
) -> AsyncIterator[tuple[str, int, int]]:
    """Async generator: (code, lap_no, lap_ms), pretending each lap arrives over the network."""
    raise NotImplementedError("Chapter 21: implement car_feed")


async def _consume(code: str, laps: int, delay_s: float, seed: int) -> tuple[str, list[int]]:
    raise NotImplementedError("Chapter 21: implement _consume")


async def collect_feeds(
    codes: list[str], laps: int, *, delay_s: float = 0.0, seed: int = 0
) -> dict[str, list[int]]:
    """Read every car's feed concurrently. Total time ~ one feed, not the sum."""
    raise NotImplementedError("Chapter 21: implement collect_feeds")


async def with_timeout(coro, seconds: float, default=None):
    """Await coro, but give up after `seconds` and return default instead."""
    raise NotImplementedError("Chapter 21: implement with_timeout")


def monte_carlo_race(seed: int, laps: int = 50, cars: int = 6) -> int:
    """Pure-Python CPU work: index of the winning car in one random race."""
    raise NotImplementedError("Chapter 21: implement monte_carlo_race")


def win_counts_threads(seeds: list[int], laps: int = 50) -> dict[int, int]:
    raise NotImplementedError("Chapter 21: implement win_counts_threads")


def win_counts_processes(seeds: list[int], laps: int = 50) -> dict[int, int]:
    raise NotImplementedError("Chapter 21: implement win_counts_processes")


def _tally(winners) -> dict[int, int]:
    raise NotImplementedError("Chapter 21: implement _tally")


class SafeCounter:
    def __init__(self):
        raise NotImplementedError("Chapter 21: implement __init__")

    def increment(self, n: int = 1) -> None:
        raise NotImplementedError("Chapter 21: implement increment")
