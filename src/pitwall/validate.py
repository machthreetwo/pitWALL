# Chapter 8 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 8: exceptions and custom errors - surviving corrupt telemetry."""

import csv
from pathlib import Path

MIN_LAP_MS = 60000
MAX_LAP_MS = 200000


class TelemetryError(Exception):
    """Base class for every PitWall data problem."""


class CorruptLapError(TelemetryError):
    """A single lap record could not be trusted."""

    def __init__(self, row: dict, reason: str):
        raise NotImplementedError("Chapter 8: implement __init__")


def parse_lap_row(row: dict) -> tuple[str, int, int]:
    """Validate one CSV row -> (driver, lap, lap_ms). Raise CorruptLapError on any problem."""
    raise NotImplementedError("Chapter 8: implement parse_lap_row")


def load_clean(rows) -> tuple[dict[str, list[int]], list[CorruptLapError]]:
    """Keep good rows (ordered by lap number per driver), collect errors for bad ones."""
    raise NotImplementedError("Chapter 8: implement load_clean")


def safe_read_laps_csv(path: str | Path) -> tuple[dict[str, list[int]], list[CorruptLapError]]:
    """Read and clean a CSV. A missing file becomes a TelemetryError (chained)."""
    raise NotImplementedError("Chapter 8: implement safe_read_laps_csv")
