# Chapter 7 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 7: files, pathlib, JSON and CSV - saving and loading sessions."""

import csv
import json
from pathlib import Path

Race = dict[str, list[int]]


def save_race_json(race: Race, path: str | Path) -> Path:
    """Write a race to JSON (pretty-printed) and return the Path written."""
    raise NotImplementedError("Chapter 7: implement save_race_json")


def load_race_json(path: str | Path) -> Race:
    """Read a race back from JSON."""
    raise NotImplementedError("Chapter 7: implement load_race_json")


def write_laps_csv(race: Race, path: str | Path) -> int:
    """Write long-format CSV (driver, lap, lap_ms). Returns rows written (excluding header)."""
    raise NotImplementedError("Chapter 7: implement write_laps_csv")


def read_laps_csv(path: str | Path) -> Race:
    """Read long-format CSV back into a race dict. CSV gives strings, so convert types."""
    raise NotImplementedError("Chapter 7: implement read_laps_csv")


def session_dir(root: str | Path, name: str) -> Path:
    """Create (if needed) and return root/sessions/name."""
    raise NotImplementedError("Chapter 7: implement session_dir")


def list_sessions(root: str | Path) -> list[str]:
    """Sorted stems of every *.json file directly inside root."""
    raise NotImplementedError("Chapter 7: implement list_sessions")
