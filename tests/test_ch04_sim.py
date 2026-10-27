import random

import pytest

from pitwall.sim import DEFAULT_GRID, best_of, log_lap, simulate_lap, simulate_race, simulate_stint


def test_simulate_lap_deterministic_parts():
    assert simulate_lap(90_000, 0) == 90_000
    assert simulate_lap(90_000, 5, deg_ms=60) == 90_300
    assert simulate_lap(90_000, 0, fuel_kg=10, kg_effect_ms=30) == 90_300


def test_simulate_lap_keyword_only():
    with pytest.raises(TypeError):
        simulate_lap(90_000, 5, 60)  # deg_ms cannot be positional


def test_noise_is_reproducible_with_seeded_rng():
    a = simulate_lap(90_000, 0, noise_ms=200, rng=random.Random(1))
    b = simulate_lap(90_000, 0, noise_ms=200, rng=random.Random(1))
    assert a == b
    assert isinstance(a, int)


def test_simulate_stint_burns_fuel():
    laps = simulate_stint(90_000, 3, fuel_start_kg=2.0, burn_kg_per_lap=1.0, deg_ms=0, kg_effect_ms=100)
    assert laps == [90_200, 90_100, 90_000]


def test_simulate_race_shape_and_seed():
    race = simulate_race(DEFAULT_GRID, 10, seed=42, noise_ms=150)
    assert set(race) == set(DEFAULT_GRID)
    assert all(len(laps) == 10 for laps in race.values())
    assert race == simulate_race(DEFAULT_GRID, 10, seed=42, noise_ms=150)
    assert race != simulate_race(DEFAULT_GRID, 10, seed=43, noise_ms=150)


def test_best_of():
    assert best_of(91_000, 90_500, 92_000) == 90_500
    with pytest.raises(ValueError):
        best_of()


def test_log_lap_does_not_share_default():
    first = log_lap(90_000)
    second = log_lap(91_000)
    assert first == [90_000]
    assert second == [91_000]
    existing = [1]
    assert log_lap(2, existing) is existing
