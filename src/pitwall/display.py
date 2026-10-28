# Chapter 2 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 2: strings, f-strings and the timing screen."""

from pitwall.units import ms_to_parts, laptime_to_ms


def format_laptime(ms: int) -> str:
    """Format milliseconds as M:SS.mmm.

    >>> format_laptime(83456)
    '1:23.456'
    """
    minutes,seconds,millis= ms_to_parts(ms)
    return f"{minutes}:{seconds:02d}.{millis:03d}" # error in seperation symbol


def format_gap(gap_ms: int) -> str:
    """Format a gap in seconds with an explicit sign and 3 decimals.

    >>> format_gap(1234)
    '+1.234'
    """
    return f"{gap_ms/1000:+.3f}"# divide by 1000 and then add positive sign in the begining


def driver_code(full_name: str) -> str:
    """Three-letter timing code from a full name: surname, first 3 letters, upper case.

    >>> driver_code("Max Verstappen")
    'VER'
    """
    a= full_name.strip().split()[-1] #first remove white spaces then split
    return a[:3].upper()


def timing_row(pos: int, name: str, lap_ms: int, gap_ms: int) -> str:
    """One fixed-width row of the timing screen.

    >>> timing_row(1, "Lando Norris", 83456, 0)
    ' 1  NOR   1:23.456    +0.000'
    """
    return f"{pos:>2}  {driver_code(name):<3}  {format_laptime(lap_ms):>9}  {format_gap(gap_ms):>8}" #needed 2 spaces iin between


def parse_laptime(text: str) -> int:
    """Inverse of format_laptime: '1:23.456' -> 83456. Surrounding whitespace is ignored."""
    min,rest=text.strip().split(":")
    sec,milli=rest.split(".")
    return laptime_to_ms(int(min),int(sec),int(milli))
