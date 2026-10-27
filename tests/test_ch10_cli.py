import logging
import subprocess
import sys

import pytest

from pitwall.cli import build_parser, main
from pitwall.storage import load_race_json


def test_parser_defaults():
    args = build_parser().parse_args(["run"])
    assert args.laps == 20 and args.seed is None and args.out is None


def test_parser_requires_command():
    with pytest.raises(SystemExit):
        build_parser().parse_args([])


def test_run_prints_classification(capsys):
    assert main(["run", "--laps", "5", "--seed", "1"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 6
    assert lines[0].startswith(" 1  ")


def test_run_then_show(tmp_path, capsys):
    out = tmp_path / "race.json"
    assert main(["run", "--laps", "3", "--seed", "7", "--out", str(out)]) == 0
    first = capsys.readouterr().out
    assert len(load_race_json(out)["Lando Norris"]) == 3
    assert main(["show", str(out)]) == 0
    assert capsys.readouterr().out == first


def test_show_missing_file_returns_1(tmp_path, caplog):
    with caplog.at_level(logging.ERROR, logger="pitwall"):
        assert main(["show", str(tmp_path / "missing.json")]) == 1
    assert "no such file" in caplog.text


def test_bad_laps_returns_2():
    assert main(["run", "--laps", "0"]) == 2


def test_python_dash_m_help():
    result = subprocess.run([sys.executable, "-m", "pitwall", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "run" in result.stdout and "show" in result.stdout
