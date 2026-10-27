import numpy as np
import pytest

from pitwall.fast import (
    cumulative, deg_slope, flag_slow_laps, gaps_to_leader_np, positions_by_lap, simulate_race_np, smooth,
)


def test_simulate_shape_and_broadcast():
    base = np.array([90_000, 90_500])
    t = simulate_race_np(base, 5, deg_ms=100, noise_ms=0)
    assert t.shape == (2, 5)
    np.testing.assert_allclose(t[0], [90_000, 90_100, 90_200, 90_300, 90_400])
    np.testing.assert_allclose(t[1] - t[0], 500)


def test_simulate_seeded():
    base = np.full(6, 90_000.0)
    np.testing.assert_array_equal(simulate_race_np(base, 10, seed=3), simulate_race_np(base, 10, seed=3))


def test_cumulative_and_positions():
    t = np.array([[10, 10, 10], [9, 12, 10], [11, 8, 13]])
    np.testing.assert_array_equal(cumulative(t), [[10, 20, 30], [9, 21, 31], [11, 19, 32]])
    np.testing.assert_array_equal(positions_by_lap(t), [[2, 2, 1], [1, 3, 2], [3, 1, 3]])
    np.testing.assert_array_equal(gaps_to_leader_np(t), [[1, 1, 0], [0, 2, 1], [2, 0, 2]])


def test_smooth():
    np.testing.assert_allclose(smooth(np.array([1.0, 2, 3, 4]), 2), [1.5, 2.5, 3.5])
    with pytest.raises(ValueError):
        smooth(np.array([1.0, 2]), 3)


def test_deg_slope_recovers_truth():
    t = simulate_race_np(np.array([90_000.0]), 30, deg_ms=75, noise_ms=50, seed=0)[0]
    assert deg_slope(t) == pytest.approx(75, abs=5)


def test_flag_slow_laps():
    t = np.array([[100.0, 101, 99, 120], [100, 100, 100, 100]])
    np.testing.assert_array_equal(flag_slow_laps(t, 1.07), [[False, False, False, True], [False] * 4])
