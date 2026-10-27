import pytest

from pitwall.stream import rolling_mean
from pitwall.toolkit import (
    chunked, consistency_ms, group_by_driver, lap_deltas, laps_per_compound, position_for_time,
    rolling_mean_fast, top_n_laps,
)


def test_top_n_laps():
    laps = [("A", 90_300), ("B", 90_100), ("C", 90_200), ("D", 91_000)]
    assert top_n_laps(laps, 2) == [("B", 90_100), ("C", 90_200)]
    assert top_n_laps(iter(laps), 10) == sorted(laps, key=lambda p: p[1])


def test_laps_per_compound():
    counts = laps_per_compound([("soft", 15), ("hard", 30), ("soft", 10)])
    assert counts == {"soft": 25, "hard": 30}
    assert counts.most_common(1) == [("hard", 30)]
    assert counts["wet"] == 0


def test_group_by_driver():
    assert group_by_driver([("A", 1), ("B", 2), ("A", 3)]) == {"A": [1, 3], "B": [2]}
    assert type(group_by_driver([])) is dict


@pytest.mark.parametrize("window", [1, 2, 3, 7])
def test_rolling_mean_fast_matches_slow(window):
    values = [90_000 + (i * 37) % 500 for i in range(50)]
    fast = list(rolling_mean_fast(values, window))
    slow = list(rolling_mean(values, window))
    assert fast == pytest.approx(slow)


def test_lap_deltas_and_consistency():
    assert lap_deltas([100, 110, 105]) == [10, -5]
    assert lap_deltas([100]) == []
    assert consistency_ms([100, 100, 100]) == 0.0
    assert consistency_ms([90, 110]) == pytest.approx(10.0)
    assert consistency_ms([5]) == 0.0


def test_chunked():
    assert chunked(range(7), 3) == [(0, 1, 2), (3, 4, 5), (6,)]


def test_position_for_time():
    totals = [100, 200, 300]
    assert position_for_time(totals, 50) == 1
    assert position_for_time(totals, 250) == 3
    assert position_for_time(totals, 200) == 3   # ties go behind the existing car
    assert position_for_time([], 1) == 1
