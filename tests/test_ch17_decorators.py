import pytest

from pitwall.decorators import counted, cumulative_deg, make_delta_tracker, retry, timed


def test_timed_preserves_metadata():
    @timed
    def lap():
        """docstring"""
        return 42

    assert lap.last_ms is None
    assert lap() == 42
    assert lap.last_ms >= 0
    assert lap.__name__ == "lap" and lap.__doc__ == "docstring"


def test_timed_records_even_on_error():
    @timed
    def boom():
        raise RuntimeError

    with pytest.raises(RuntimeError):
        boom()
    assert boom.last_ms is not None


def test_retry_eventually_succeeds():
    attempts = []

    @retry(times=3, exceptions=(ConnectionError,))
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ConnectionError("feed dropped")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 3


def test_retry_gives_up_and_ignores_other_errors():
    @retry(times=2, exceptions=(ConnectionError,))
    def always_down():
        raise ConnectionError

    with pytest.raises(ConnectionError):
        always_down()

    calls = []

    @retry(times=5, exceptions=(ConnectionError,))
    def bug():
        calls.append(1)
        raise KeyError("not retried")

    with pytest.raises(KeyError):
        bug()
    assert len(calls) == 1
    with pytest.raises(ValueError):
        retry(times=0)


def test_counted():
    @counted
    def f(x):
        return x * 2

    f(1), f(2)
    assert f.calls == 2


def test_delta_tracker_closures_are_independent():
    a, b = make_delta_tracker(90_000), make_delta_tracker(90_000)
    assert a(90_200) == 200
    assert a(89_900) == 100
    assert b(90_000) == 0


def test_cumulative_deg():
    cumulative_deg.cache_clear()
    assert cumulative_deg(100, 1) == 0
    assert cumulative_deg(100, 4) == 0 + 100 + 200 + 300
    assert cumulative_deg(80, 500) == 80 * sum(range(500))
    assert cumulative_deg.cache_info().hits >= 0
