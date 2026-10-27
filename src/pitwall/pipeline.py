# Chapter 28 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 28: integration - one command for a whole race weekend."""

import logging
from pathlib import Path
import numpy as np
from pitwall.analysis import add_stints, array_to_df, drop_slow_laps, stint_summary
from pitwall.db import RaceDB
from pitwall.display import format_laptime
from pitwall.fast import simulate_race_np
from pitwall.plots import plot_lap_times, save_figure
from pitwall.predict import make_training_data, save_model, train_deg_model
from pitwall.sim import DEFAULT_GRID

log = logging.getLogger("pitwall.pipeline")


def run_weekend(out_dir: str | Path, *, laps: int = 30, seed: int = 7, pit_lap: int | None = None) -> dict:
    """Simulate -> store -> analyse -> plot -> train. Returns a summary dict.

    Every stage is a function from an earlier chapter; this one only wires them.
    """
    raise NotImplementedError("Chapter 28: implement run_weekend")
