# Chapter 24 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 24: matplotlib - lap-time and degradation plots."""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_lap_times(df: pd.DataFrame, ax=None):
    """One line per driver: lap number vs lap time (s). Returns the Axes."""
    raise NotImplementedError("Chapter 24: implement plot_lap_times")


def plot_degradation(df: pd.DataFrame, driver: str, ax=None):
    """Scatter one driver's laps per stint with a fitted trend line each."""
    raise NotImplementedError("Chapter 24: implement plot_degradation")


def save_figure(ax, path: str | Path, dpi: int = 120) -> Path:
    """Save the figure that owns ax, close it (free memory), return the path."""
    raise NotImplementedError("Chapter 24: implement save_figure")
