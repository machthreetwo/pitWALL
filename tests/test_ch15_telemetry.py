import dataclasses

import pytest

from pitwall.telemetry import ListSource, Sample, StintRecord, TelemetrySource, full_throttle_ratio, max_speed


def test_sample_is_frozen_and_validated():
    s = Sample(0, 300.0, 1.0, False, 8)
    with pytest.raises(dataclasses.FrozenInstanceError):
        s.speed_kmh = 1.0
    for bad in [dict(throttle=1.5), dict(gear=9), dict(speed_kmh=-1.0)]:
        kwargs = dict(t_ms=0, speed_kmh=100.0, throttle=0.5, brake=False, gear=3) | bad
        with pytest.raises(ValueError):
            Sample(**kwargs)


def test_sample_equality_and_replace():
    s = Sample(0, 300.0, 1.0, False, 8)
    assert s == Sample(0, 300.0, 1.0, False, 8)
    assert dataclasses.replace(s, gear=7).gear == 7


def test_stint_record_default_factory():
    a, b = StintRecord("VER", "soft"), StintRecord("NOR", "hard")
    a.add(90_000)
    a.add(90_200)
    assert b.laps == []
    assert a.avg_ms == 90_100
    assert StintRecord("X", "soft").avg_ms == 0.0


def test_protocol_structural_typing():
    samples = [Sample(0, 250.0, 1.0, False, 7), Sample(100, 310.5, 0.995, False, 8), Sample(200, 90.0, 0.0, True, 3)]
    src = ListSource(samples)
    assert isinstance(src, TelemetrySource)          # no inheritance needed
    assert not issubclass(ListSource, Sample)
    assert max_speed(src) == 310.5
    assert full_throttle_ratio(src) == pytest.approx(2 / 3)
    assert max_speed(ListSource([])) == 0.0
