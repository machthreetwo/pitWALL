# Chapter 2 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 2: strings, f-strings and the timing screen."""

from pitwall.units import ms_to_parts, laptime_to_ms


def format_laptime(ms: int) -> str:
    """Format milliseconds as M:SS.mmm.

    >>> format_laptime(83456)
    '1:23.456'
    """
    minutes,seconds,millis= ms_to_parts
    return f"{minutes}:{seconds:02d}:{millis:03d}"


def format_gap(gap_ms: int) -> str:
    """Format a gap in seconds with an explicit sign and 3 decimals.

    >>> format_gap(1234)
    '+1.234'
    """
    return f"{gap_ms/1000:+}"# divide by 1000 and then add positive sign in the begining


def driver_code(full_name: str) -> str:
    """Three-letter timing code from a full name: surname, first 3 letters, upper case.

    >>> driver_code("Max Verstappen")
    'VER'
    """
    raise NotImplementedError("Chapter 2: implement driver_code")


def timing_row(pos: int, name: str, lap_ms: int, gap_ms: int) -> str:
    """One fixed-width row of the timing screen.

    >>> timing_row(1, "Lando Norris", 83456, 0)
    ' 1  NOR   1:23.456    +0.000'
    """
    raise NotImplementedError("Chapter 2: implement timing_row")


def parse_laptime(text: str) -> int:
    """Inverse of format_laptime: '1:23.456' -> 83456. Surrounding whitespace is ignored."""
    raise NotImplementedError("Chapter 2: implement parse_laptime")
