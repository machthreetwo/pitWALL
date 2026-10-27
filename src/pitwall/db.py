# Chapter 25 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 25: sqlite3 and SQL - a persistent race database."""

import sqlite3
from pathlib import Path
import pandas as pd

SCHEMA = "-- TODO Chapter 25: CREATE TABLE races, CREATE TABLE laps, CREATE INDEX"


class RaceDB:
    """Thin wrapper over sqlite3. Use as a context manager so it always closes."""

    def __init__(self, path: str | Path = ":memory:", *, check_same_thread: bool = True):
        raise NotImplementedError("Chapter 25: implement __init__")

    def __enter__(self) -> "RaceDB":
        raise NotImplementedError("Chapter 25: implement __enter__")

    def __exit__(self, *exc) -> None:
        raise NotImplementedError("Chapter 25: implement __exit__")

    def close(self) -> None:
        raise NotImplementedError("Chapter 25: implement close")

    def insert_race(self, name: str, race: dict[str, list[int]]) -> int:
        """Insert a race and all its laps in ONE transaction. Returns the race id."""
        raise NotImplementedError("Chapter 25: implement insert_race")

    def race_id(self, name: str) -> int | None:
        raise NotImplementedError("Chapter 25: implement race_id")

    def fastest_laps(self, race_id: int) -> list[tuple[str, int]]:
        """Each driver's best lap, fastest first."""
        raise NotImplementedError("Chapter 25: implement fastest_laps")

    def classification(self, race_id: int) -> list[tuple[str, int, int]]:
        """(driver, laps_completed, total_ms) ordered by laps desc then total asc."""
        raise NotImplementedError("Chapter 25: implement classification")

    def laps_df(self, race_id: int) -> pd.DataFrame:
        raise NotImplementedError("Chapter 25: implement laps_df")

    def delete_race(self, race_id: int) -> None:
        raise NotImplementedError("Chapter 25: implement delete_race")
