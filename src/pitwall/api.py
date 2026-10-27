# Chapter 27 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 27: FastAPI + Pydantic - serving telemetry and predictions."""

from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pitwall.db import RaceDB
from pitwall.predict import make_training_data, predict_lap_delta, train_deg_model
from pitwall.sim import DEFAULT_GRID, simulate_race


class SimRequest(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    laps: int = Field(default=20, ge=1, le=100)
    seed: int | None = None
    noise_ms: float = Field(default=150.0, ge=0)
    drivers: dict[str, int] | None = None


class StandingRow(BaseModel):
    position: int
    driver: str
    laps: int
    total_ms: int
    gap_ms: int


class RaceCreated(BaseModel):
    race_id: int
    name: str
    standings: list[StandingRow]


class PredictRequest(BaseModel):
    compound: Literal["soft", "medium", "hard"]
    tyre_age: int = Field(ge=0, le=80)
    fuel_kg: float = Field(ge=0, le=120)
    track_temp: float = Field(ge=0, le=70)


class PredictResponse(BaseModel):
    lap_delta_ms: float


def create_app(db_path: str = ":memory:", model=None) -> FastAPI:
    """App factory: each call builds an independent app (handy for tests)."""
    raise NotImplementedError("Chapter 27: implement create_app")
