from pitwall.storage import (
    list_sessions, load_race_json, read_laps_csv, save_race_json, session_dir, write_laps_csv,
)


def test_json_round_trip(tmp_path, small_race):
    path = save_race_json(small_race, tmp_path / "nested" / "race.json")
    assert path.exists()
    assert load_race_json(path) == small_race


def test_csv_round_trip(tmp_path, small_race):
    path = tmp_path / "laps.csv"
    assert write_laps_csv(small_race, path) == 12
    assert path.read_text().splitlines()[0] == "driver,lap,lap_ms"
    loaded = read_laps_csv(path)
    assert loaded == small_race
    assert all(isinstance(ms, int) for laps in loaded.values() for ms in laps)


def test_session_dir(tmp_path):
    d = session_dir(tmp_path, "monza")
    assert d == tmp_path / "sessions" / "monza"
    assert d.is_dir()
    assert session_dir(tmp_path, "monza") == d  # idempotent


def test_list_sessions(tmp_path):
    for name in ("spa", "monza", "notes"):
        suffix = ".txt" if name == "notes" else ".json"
        (tmp_path / f"{name}{suffix}").write_text("{}")
    assert list_sessions(tmp_path) == ["monza", "spa"]
