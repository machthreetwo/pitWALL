import asyncio
import threading
import time

import pytest

from pitwall.live import (
    SafeCounter, car_feed, collect_feeds, monte_carlo_race, win_counts_processes, win_counts_threads, with_timeout,
)


def test_car_feed_is_async_generator():
    async def first_three():
        return [item async for item in car_feed("VER", 3)]

    items = asyncio.run(first_three())
    assert [(c, n) for c, n, _ in items] == [("VER", 1), ("VER", 2), ("VER", 3)]
    assert all(89_600 <= ms <= 90_400 for _, _, ms in items)


def test_collect_feeds_runs_concurrently():
    codes = ["VER", "NOR", "LEC", "PIA", "HAM"]
    start = time.perf_counter()
    result = asyncio.run(collect_feeds(codes, laps=4, delay_s=0.05, seed=1))
    elapsed = time.perf_counter() - start
    assert set(result) == set(codes) and all(len(v) == 4 for v in result.values())
    assert elapsed < 0.6   # sequential would be 5 * 4 * 0.05 = 1.0 s
    assert result == asyncio.run(collect_feeds(codes, laps=4, seed=1))   # seeded per car


def test_with_timeout():
    async def slow():
        await asyncio.sleep(1)
        return "late"

    async def fast():
        return "ok"

    assert asyncio.run(with_timeout(slow(), 0.05, default="timeout")) == "timeout"
    assert asyncio.run(with_timeout(fast(), 1)) == "ok"


def test_monte_carlo_deterministic():
    assert monte_carlo_race(5) == monte_carlo_race(5)
    assert 0 <= monte_carlo_race(5) < 6


@pytest.mark.slow
def test_threads_and_processes_agree():
    seeds = list(range(40))
    threads = win_counts_threads(seeds, laps=20)
    procs = win_counts_processes(seeds, laps=20)
    assert threads == procs
    assert sum(threads.values()) == 40


def test_safe_counter():
    counter = SafeCounter()

    def work():
        for _ in range(10_000):
            counter.increment()

    threads = [threading.Thread(target=work) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter.value == 80_000
