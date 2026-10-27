import pytest

from pitwall.validate import CorruptLapError, TelemetryError, load_clean, parse_lap_row, safe_read_laps_csv


def test_parse_good_row():
    assert parse_lap_row({"driver": " VER ", "lap": "3", "lap_ms": "90500"}) == ("VER", 3, 90_500)


@pytest.mark.parametrize(
    "row, reason_part",
    [
        ({"lap": "1", "lap_ms": "90000"}, "missing field driver"),
        ({"driver": "VER", "lap": "x", "lap_ms": "90000"}, "non-numeric"),
        ({"driver": "VER", "lap": "1", "lap_ms": None}, "non-numeric"),
        ({"driver": "", "lap": "1", "lap_ms": "90000"}, "empty driver"),
        ({"driver": "VER", "lap": "0", "lap_ms": "90000"}, "lap number"),
        ({"driver": "VER", "lap": "1", "lap_ms": "5000"}, "out of range"),
    ],
)
def test_parse_bad_rows(row, reason_part):
    with pytest.raises(CorruptLapError) as info:
        parse_lap_row(row)
    assert reason_part in info.value.reason
    assert info.value.row is row


def test_error_hierarchy():
    assert issubclass(CorruptLapError, TelemetryError)
    assert issubclass(TelemetryError, Exception)


def test_load_clean_keeps_going_and_sorts():
    rows = [
        {"driver": "VER", "lap": "2", "lap_ms": "90200"},
        {"driver": "VER", "lap": "1", "lap_ms": "90100"},
        {"driver": "VER", "lap": "3", "lap_ms": "garbage"},
        {"driver": "NOR", "lap": "1", "lap_ms": "90000"},
    ]
    race, errors = load_clean(rows)
    assert race == {"VER": [90_100, 90_200], "NOR": [90_000]}
    assert len(errors) == 1


def test_missing_file_is_chained(tmp_path):
    with pytest.raises(TelemetryError) as info:
        safe_read_laps_csv(tmp_path / "nope.csv")
    assert isinstance(info.value.__cause__, FileNotFoundError)


def test_safe_read(tmp_path):
    p = tmp_path / "laps.csv"
    p.write_text("driver,lap,lap_ms\nVER,1,90000\nVER,2,1\n")
    race, errors = safe_read_laps_csv(p)
    assert race == {"VER": [90_000]}
    assert len(errors) == 1
