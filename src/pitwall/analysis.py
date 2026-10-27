# Chapter 23 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 23: pandas - session analysis."""

import numpy as np
import pandas as pd


def race_to_df(race: dict[str, list[int]]) -> pd.DataFrame:
    """Long ('tidy') format: one row per (driver, lap). Columns: driver, lap, lap_ms, lap_s."""
    raise NotImplementedError("Chapter 23: implement race_to_df")


def array_to_df(times: np.ndarray, drivers: list[str]) -> pd.DataFrame:
    """Same long format from a (n_cars, laps) NumPy array (Chapter 22 output)."""
    raise NotImplementedError("Chapter 23: implement array_to_df")


def add_stints(df: pd.DataFrame, pit_laps: dict[str, list[int]]) -> pd.DataFrame:
    """Add a 1-based `stint` column. A pit on lap p means lap p+1 starts the next stint."""
    raise NotImplementedError("Chapter 23: implement add_stints")


def drop_slow_laps(df: pd.DataFrame, pct: float = 1.07) -> pd.DataFrame:
    """Remove laps slower than pct x the driver's median (in/out laps, safety car)."""
    raise NotImplementedError("Chapter 23: implement drop_slow_laps")


def stint_summary(df: pd.DataFrame) -> pd.DataFrame:
    """One row per (driver, stint): laps, mean_ms, best_ms, deg_ms_per_lap."""
    raise NotImplementedError("Chapter 23: implement stint_summary")


def pace_table(df: pd.DataFrame) -> pd.DataFrame:
    """Wide view: drivers as rows, lap numbers as columns, lap_ms as values."""
    raise NotImplementedError("Chapter 23: implement pace_table")


def rolling_pace(df: pd.DataFrame, window: int = 3) -> pd.Series:
    """Rolling mean lap time within each driver (never mixes drivers)."""
    raise NotImplementedError("Chapter 23: implement rolling_pace")


def merge_driver_info(df: pd.DataFrame, info: pd.DataFrame) -> pd.DataFrame:
    """Left-join team info onto laps. Fails loudly if info has duplicate drivers."""
    raise NotImplementedError("Chapter 23: implement merge_driver_info")
