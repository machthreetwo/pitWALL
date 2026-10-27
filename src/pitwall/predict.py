# Chapter 26 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 26: scikit-learn - a tyre-degradation predictor."""

from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

FEATURES = ["compound", "tyre_age", "fuel_kg", "track_temp"]
TARGET = "lap_delta_ms"
_DEG = {"soft": 110, "medium": 75, "hard": 50}
_OFFSET = {"soft": 0, "medium": 350, "hard": 700}
_LIFE = {"soft": 18, "medium": 28, "hard": 40}


def make_training_data(n: int = 3000, seed: int = 0) -> pd.DataFrame:
    """Synthetic laps: features + lap_delta_ms (time lost vs a perfect lap).

    Non-linear on purpose: past the tyre's life, time falls off a cliff, and hot
    track temperatures accelerate degradation.
    """
    rng = np.random.default_rng(seed)
    compound = rng.choice(list(_DEG), size=n)
    age = rng.integers(0, 45, size=n)
    fuel = rng.uniform(0, 110, size=n)
    temp = rng.uniform(20, 55, size=n)
    deg = np.array([_DEG[c] for c in compound])
    offset = np.array([_OFFSET[c] for c in compound])
    life = np.array([_LIFE[c] for c in compound])
    heat = 1 + (temp - 35) / 60
    cliff = np.where(age > life, (age - life) * 250, 0)
    delta = offset + deg * age * heat + cliff + fuel * 30 + rng.normal(0, 120, size=n)
    return pd.DataFrame(
        {
            "compound": compound,
            "tyre_age": age,
            "fuel_kg": fuel.round(1),
            "track_temp": temp.round(1),
            TARGET: delta.round(),
        }
    )


def build_pipeline(kind: str = "forest") -> Pipeline:
    """One-hot the compound, pass numbers through, then a regressor."""
    raise NotImplementedError("Chapter 26: implement build_pipeline")


def train_deg_model(df: pd.DataFrame, *, kind: str = "forest", test_size: float = 0.2, seed: int = 0):
    """Fit on a train split, score on the held-out test split. Returns (pipeline, metrics)."""
    raise NotImplementedError("Chapter 26: implement train_deg_model")


def predict_lap_delta(
    model: Pipeline, compound: str, tyre_age: int, fuel_kg: float, track_temp: float
) -> float:
    raise NotImplementedError("Chapter 26: implement predict_lap_delta")


def save_model(model: Pipeline, path: str | Path) -> Path:
    raise NotImplementedError("Chapter 26: implement save_model")


def load_model(path: str | Path) -> Pipeline:
    raise NotImplementedError("Chapter 26: implement load_model")
