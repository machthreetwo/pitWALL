# Chapter 10 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 10: logging and argparse - the `pitwall` command line."""

import argparse
import logging
from pitwall.display import timing_row
from pitwall.sim import DEFAULT_GRID, simulate_race
from pitwall.standings import classify, gaps_to_leader
from pitwall.storage import load_race_json, save_race_json

log = logging.getLogger("pitwall")


def configure_logging(verbose: bool = False) -> None:
    """INFO by default, DEBUG with --verbose. Safe to call more than once.

    Configures the `pitwall` logger only - never the root logger - so importing
    PitWall into someone else's app does not hijack their logging.
    """
    raise NotImplementedError("Chapter 10: implement configure_logging")


def build_parser() -> argparse.ArgumentParser:
    """Parser with two subcommands: `run` and `show`."""
    raise NotImplementedError("Chapter 10: implement build_parser")


def render_classification(race: dict[str, list[int]]) -> list[str]:
    """Timing-screen lines, using each driver's last lap as the lap column."""
    raise NotImplementedError("Chapter 10: implement render_classification")


def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns a process exit code instead of calling sys.exit()."""
    raise NotImplementedError("Chapter 10: implement main")
