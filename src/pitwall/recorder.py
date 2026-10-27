# Chapter 18 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 18: context managers - recording a session safely."""

import json
import time
from contextlib import contextmanager
from pathlib import Path


class SessionRecorder:
    """`with SessionRecorder(path) as rec: rec.record({...})`

    Writes one JSON object per line (JSONL). On exit it ALWAYS writes an `end`
    event, even if the block raised, then closes the file. Exceptions are not
    swallowed.
    """

    def __init__(self, path: str | Path):
        raise NotImplementedError("Chapter 18: implement __init__")

    def __enter__(self) -> "SessionRecorder":
        raise NotImplementedError("Chapter 18: implement __enter__")

    def record(self, data: dict) -> None:
        raise NotImplementedError("Chapter 18: implement record")

    def __exit__(self, exc_type, exc, tb) -> bool:
        raise NotImplementedError("Chapter 18: implement __exit__")

    def _write(self, obj: dict) -> None:
        raise NotImplementedError("Chapter 18: implement _write")


def read_recording(path: str | Path) -> list[dict]:
    raise NotImplementedError("Chapter 18: implement read_recording")


@contextmanager
def stopwatch():
    """Yields a dict; after the block, result['ms'] holds the elapsed milliseconds."""
    raise NotImplementedError("Chapter 18: implement stopwatch")


@contextmanager
def temp_setting(obj, attr: str, value):
    """Temporarily set obj.attr = value, restoring the old value no matter what."""
    raise NotImplementedError("Chapter 18: implement temp_setting")
