# Chapter 17 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 17: closures and decorators - @timed, @retry, @counted, caching."""

import functools
import logging
import time

log = logging.getLogger("pitwall.decorators")


def timed(func):
    """Measure each call; the last duration (ms) is stored on wrapper.last_ms."""
    raise NotImplementedError("Chapter 17: implement timed")


def retry(times: int = 3, exceptions: tuple[type[BaseException], ...] = (Exception,), delay_s: float = 0.0):
    """Decorator FACTORY: retry() returns the real decorator."""
    raise NotImplementedError("Chapter 17: implement retry")


def counted(func):
    """Count calls on wrapper.calls."""
    raise NotImplementedError("Chapter 17: implement counted")


def make_delta_tracker(reference_ms: int):
    """Closure: returns a function that accumulates the delta to a reference lap.

    track = make_delta_tracker(90_000); track(90_200) -> 200; track(89_900) -> 100
    """
    raise NotImplementedError("Chapter 17: implement make_delta_tracker")


@functools.cache
def cumulative_deg(deg_ms: int, laps: int) -> int:
    """Total degradation over a stint: deg*0 + deg*1 + ... + deg*(laps-1). Recursive + cached."""
    raise NotImplementedError("Chapter 17: implement cumulative_deg")
