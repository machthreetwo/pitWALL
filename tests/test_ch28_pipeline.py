from pathlib import Path

import pandas as pd
import pytest

from pitwall.cli import main
from pitwall.pipeline import run_weekend


@pytest.mark.slow
def test_run_weekend(tmp_path):
    summary = run_weekend(tmp_path, laps=20, seed=3)
    for key in ("db_path", "plot_path", "stints_path", "model_path"):
        assert Path(summary[key]).exists(), key
    stints = pd.read_csv(summary["stints_path"])
    assert set(stints["stint"]) == {1, 2}
    assert summary["winner"] in {"Lando Norris", "Max Verstappen", "Oscar Piastri", "Charles Leclerc",
                                 "George Russell", "Lewis Hamilton"}
    assert summary["model_mae_ms"] < 400
    # running twice must not crash on the UNIQUE race name
    assert run_weekend(tmp_path, laps=20, seed=3)["winner"] == summary["winner"]


@pytest.mark.slow
def test_cli_weekend(tmp_path, capsys):
    assert main(["weekend", "--out", str(tmp_path), "--laps", "10"]) == 0
    assert "winner" in capsys.readouterr().out
