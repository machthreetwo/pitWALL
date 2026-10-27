# Chapter 22 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 22: NumPy - vectorising the simulator."""

import numpy as np


def simulate_race_np(
    base_ms: np.ndarray, laps: int, *, deg_ms: float = 80.0, noise_ms: float = 150.0, seed: int | None = None
) -> np.ndarray:
    """Lap times as a (n_cars, laps) float array - no Python loops.

    base_ms[:, None] has shape (n, 1); np.arange(laps)[None, :] has shape (1, laps).
    Broadcasting stretches both to (n, laps).
    """
    raise NotImplementedError("Chapter 22: implement simulate_race_np")


def cumulative(times: np.ndarray) -> np.ndarray:
    """Running race time for every car after every lap."""
    raise NotImplementedError("Chapter 22: implement cumulative")


def positions_by_lap(times: np.ndarray) -> np.ndarray:
    """1-based running position of each car at the end of each lap, shape (n_cars, laps).

    argsort gives the ORDER; argsort of that order gives each car's RANK.
    """
    raise NotImplementedError("Chapter 22: implement positions_by_lap")


def gaps_to_leader_np(times: np.ndarray) -> np.ndarray:
    """Gap to whoever is leading at the end of each lap."""
    raise NotImplementedError("Chapter 22: implement gaps_to_leader_np")


def smooth(signal: np.ndarray, window: int) -> np.ndarray:
    """Moving average via convolution; output length = len(signal) - window + 1."""
    raise NotImplementedError("Chapter 22: implement smooth")


def deg_slope(laptimes: np.ndarray) -> float:
    """Least-squares slope (ms per lap) of a stint's lap times."""
    raise NotImplementedError("Chapter 22: implement deg_slope")


def flag_slow_laps(times: np.ndarray, pct: float = 1.07) -> np.ndarray:
    """Boolean mask: laps slower than pct x that car's median lap (boolean indexing)."""
    raise NotImplementedError("Chapter 22: implement flag_slow_laps")
