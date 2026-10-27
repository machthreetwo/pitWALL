import inspect
import itertools

import pytest

from pitwall.stream import LapClock, braking_zones, rolling_mean, speeds, take, telemetry_stream
from pitwall.telemetry import Sample


def test_lap_clock_iterator_protocol():
    clock = LapClock(3)
    assert iter(clock) is clock
    assert list(clock) == [1, 2, 3]
    assert list(clock) == []          # exhausted iterators stay exhausted


def test_stream_is_lazy_and_reproducible():
    gen = telemetry_stream(10**9, seed=1)    # a billion samples: only OK because it's lazy
    assert inspect.isgenerator(gen)
    first = list(take(5, gen))
    assert all(isinstance(s, Sample) for s in first)
    assert [s.t_ms for s in first] == [0, 100, 200, 300, 400]
    assert first == list(take(5, telemetry_stream(10**9, seed=1)))


def test_take_on_infinite_iterator():
    assert list(take(3, itertools.count())) == [0, 1, 2]
    assert list(take(0, itertools.count())) == []


def test_rolling_mean():
    assert list(rolling_mean([1, 2, 3, 4, 5], 2)) == [1.5, 2.5, 3.5, 4.5]
    assert list(rolling_mean([1, 2], 3)) == []
    with pytest.raises(ValueError):
        list(rolling_mean([1], 0))


def mk(t, brake):
    return Sample(t, 100.0, 0.0 if brake else 1.0, brake, 3)


def test_braking_zones():
    samples = [mk(0, False), mk(1, True), mk(2, True), mk(3, False), mk(4, True)]
    assert list(braking_zones(samples)) == [(1, 2), (4, 4)]


def test_generated_lap_has_braking_and_pipeline_works():
    lap = list(telemetry_stream(200, seed=3))
    assert len(list(braking_zones(lap))) == 4
    top = max(speeds(lap))
    assert 300 < top < 340
