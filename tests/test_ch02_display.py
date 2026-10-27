import pytest

from pitwall.display import driver_code, format_gap, format_laptime, parse_laptime, timing_row


@pytest.mark.parametrize("ms, text", [(83_456, "1:23.456"), (60_005, "1:00.005"), (9_870, "0:09.870")])
def test_format_laptime(ms, text):
    assert format_laptime(ms) == text


def test_format_gap():
    assert format_gap(1234) == "+1.234"
    assert format_gap(0) == "+0.000"
    assert format_gap(-500) == "-0.500"


@pytest.mark.parametrize(
    "name, code",
    [("Max Verstappen", "VER"), ("  lando norris ", "NOR"), ("Andrea Kimi Antonelli", "ANT"), ("Zhou", "ZHO")],
)
def test_driver_code(name, code):
    assert driver_code(name) == code


def test_timing_row_is_fixed_width():
    a = timing_row(1, "Lando Norris", 83_456, 0)
    b = timing_row(12, "Charles Leclerc", 101_002, 12_345)
    assert a == " 1  NOR   1:23.456    +0.000"
    assert len(a) == len(b)


def test_parse_laptime_round_trip():
    assert parse_laptime(" 1:23.456 ") == 83_456
    for ms in (0, 9_870, 83_456, 125_001):
        assert parse_laptime(format_laptime(ms)) == ms
