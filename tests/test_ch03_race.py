import pytest

from pitwall.race import count_in_window, first_lap_over, laps_until_cliff, stint_laptimes, tyre_life, tyre_state


def test_tyre_life():
    assert (tyre_life("soft"), tyre_life("medium"), tyre_life("hard")) == (18, 28, 40)
    assert tyre_life("wet") == 0


@pytest.mark.parametrize(
    "age, compound, state",
    [
        (0, "soft", "fresh"), (3, "soft", "fresh"), (4, "soft", "ok"),
        (13, "soft", "worn"),   # 0.7 * 18 = 12.6
        (18, "soft", "cliff"), (19, "medium", "ok"), (20, "medium", "worn"),   # 0.7 * 28 = 19.6
        (40, "hard", "cliff"), (5, "intermediate", "unknown"),
    ],
)
def test_tyre_state(age, compound, state):
    assert tyre_state(age, compound) == state


def test_stint_laptimes():
    assert stint_laptimes(90_000, 3, 100) == [90_000, 90_100, 90_200]
    assert stint_laptimes(90_000, 0, 100) == []


def test_first_lap_over():
    laps = [90_000, 90_100, 90_900, 91_000]
    assert first_lap_over(laps, 90_500) == 3
    assert first_lap_over(laps, 99_999) == -1
    assert first_lap_over([], 1) == -1


def test_laps_until_cliff():
    assert laps_until_cliff("soft", 10) == 8
    assert laps_until_cliff("soft", 25) == 0
    assert laps_until_cliff("wet", 0) == 0


def test_count_in_window():
    assert count_in_window([1, 5, 10, 15], 5, 10) == 2
