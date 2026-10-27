# Chapter 11 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 11: regular expressions - parsing team radio and logs."""

import re
from pitwall.display import parse_laptime

RADIO_LINE = re.compile("(?!)")
LAPTIME = re.compile("(?!)")
BOX_CALL = re.compile("(?!)")


def parse_radio(line: str) -> dict | None:
    """Parse one radio line into a dict, or None if it does not match.

    Keys: lap (int), time, sender, receiver, message.
    """
    raise NotImplementedError("Chapter 11: implement parse_radio")


def extract_laptimes(text: str) -> list[int]:
    """Every M:SS.mmm lap time mentioned anywhere in text, as ms."""
    raise NotImplementedError("Chapter 11: implement extract_laptimes")


def box_calls(lines: list[str]) -> list[int]:
    """Lap numbers of radio messages that contain the whole word 'box'."""
    raise NotImplementedError("Chapter 11: implement box_calls")


def redact_laptimes(text: str) -> str:
    """Replace every lap time with X:XX.XXX (e.g. before sharing radio publicly)."""
    raise NotImplementedError("Chapter 11: implement redact_laptimes")
