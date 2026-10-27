# Chapter 1 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 1: lap-time arithmetic and unit conversion.

Everything in PitWall stores time as an integer number of milliseconds.
Integers are exact; floats are not. That one decision removes a whole
class of bugs (0.1 + 0.2 != 0.3) from every later chapter.
"""

MS_PER_SECOND = 1000
MS_PER_MINUTE = 60 * MS_PER_SECOND


def laptime_to_ms(minutes: int, seconds: int, millis: int) -> int:
    """Convert a lap time given as parts into total milliseconds.

    >>> laptime_to_ms(1, 23, 456)
    83456
    """
    raise NotImplementedError("Chapter 1: implement laptime_to_ms")


def ms_to_parts(ms: int) -> tuple[int, int, int]:
    """Split milliseconds into (minutes, seconds, millis).

    >>> ms_to_parts(83456)
    (1, 23, 456)
    """
    raise NotImplementedError("Chapter 1: implement ms_to_parts")


def kmh_to_ms(kmh: float) -> float:
    """Convert km/h to metres per second."""
    raise NotImplementedError("Chapter 1: implement kmh_to_ms")


def avg_speed_kmh(track_km: float, lap_ms: int) -> float:
    """Average speed over a lap, rounded to 3 decimal places."""
    raise NotImplementedError("Chapter 1: implement avg_speed_kmh")


def fuel_needed_kg(laps: int, kg_per_lap: float, margin_laps: int) -> float:
    """Fuel to load for a race distance plus a safety margin of extra laps."""
    raise NotImplementedError("Chapter 1: implement fuel_needed_kg")


def is_faster(a_ms: int, b_ms: int) -> bool:
    """True if lap a is strictly faster than lap b."""
    raise NotImplementedError("Chapter 1: implement is_faster")
