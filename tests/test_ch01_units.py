import pytest

from pitwall.units import avg_speed_kmh, fuel_needed_kg, is_faster, kmh_to_ms, laptime_to_ms, ms_to_parts


def test_laptime_to_ms():
    assert laptime_to_ms(1, 23, 456) == 83_456
    assert laptime_to_ms(0, 0, 0) == 0
    assert isinstance(laptime_to_ms(1, 30, 0), int)


@pytest.mark.parametrize("ms, parts", [(83_456, (1, 23, 456)), (59_999, (0, 59, 999)), (60_000, (1, 0, 0))])
def test_ms_to_parts(ms, parts):
    assert ms_to_parts(ms) == parts


def test_round_trip():
    for ms in (0, 1, 999, 1000, 61_001, 125_432):
        assert laptime_to_ms(*ms_to_parts(ms)) == ms


def test_kmh_to_ms():
    assert kmh_to_ms(36) == pytest.approx(10.0)
    assert kmh_to_ms(0) == 0


def test_avg_speed():
    # Monza-ish: 5.793 km in 1:21.000
    assert avg_speed_kmh(5.793, 81_000) == pytest.approx(257.467, abs=0.001)


def test_fuel_and_compare():
    assert fuel_needed_kg(50, 1.6, 2) == pytest.approx(83.2)
    assert is_faster(90_000, 90_001) is True
    assert is_faster(90_000, 90_000) is False
