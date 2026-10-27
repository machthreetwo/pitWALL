import pytest

from pitwall.recorder import SessionRecorder, read_recording, stopwatch, temp_setting


def test_recorder_happy_path(tmp_path):
    path = tmp_path / "rec" / "s.jsonl"
    with SessionRecorder(path) as rec:
        rec.record({"driver": "VER", "lap": 1, "ms": 90_000})
        rec.record({"driver": "VER", "lap": 2, "ms": 90_100})
    events = read_recording(path)
    assert [e["event"] for e in events] == ["start", "lap", "lap", "end"]
    assert events[-1] == {"event": "end", "laps": 2, "error": None}


def test_recorder_writes_footer_and_reraises(tmp_path):
    path = tmp_path / "s.jsonl"
    with pytest.raises(ZeroDivisionError):
        with SessionRecorder(path) as rec:
            rec.record({"lap": 1})
            1 / 0
    assert read_recording(path)[-1] == {"event": "end", "laps": 1, "error": "ZeroDivisionError"}


def test_record_outside_with_fails(tmp_path):
    rec = SessionRecorder(tmp_path / "x.jsonl")
    with pytest.raises(RuntimeError):
        rec.record({})


def test_stopwatch():
    with stopwatch() as sw:
        assert sw["ms"] is None
        sum(range(10_000))
    assert sw["ms"] > 0


def test_temp_setting_restores_even_on_error():
    class Config:
        noise_ms = 150

    cfg = Config()
    with pytest.raises(KeyError):
        with temp_setting(cfg, "noise_ms", 0):
            assert cfg.noise_ms == 0
            raise KeyError
    assert cfg.noise_ms == 150
