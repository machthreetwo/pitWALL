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
    return (minutes*MS_PER_MINUTE +seconds*MS_PER_SECOND+millis)
    


def ms_to_parts(ms: int) -> tuple[int, int, int]:
    """Split milliseconds into (minutes, seconds, millis).

    >>> ms_to_parts(83456)
    (1, 23, 456)
    """
    minutes,rest= divmod(ms, MS_PER_MINUTE) #one minutes has 60X1000 milliseconds
    seconds,millis=divmod(rest,MS_PER_SECOND)  #One second has 1000 milliseconds
    return minutes,seconds,millis # failed first test due to absence of this line


def kmh_to_ms(kmh: float) -> float:
    """Convert km/h to metres per second."""
    return kmh *5/18


def avg_speed_kmh(track_km: float, lap_ms: int) -> float:
    """Average speed over a lap, rounded to 3 decimal places."""
    hours=lap_ms/MS_PER_SECOND/3600
    return round(track_km/hours,3)
    


def fuel_needed_kg(laps: int, kg_per_lap: float, margin_laps: int) -> float:
    """Fuel to load for a race distance plus a safety margin of extra laps."""
    return (laps+margin_laps)*kg_per_lap

    


def is_faster(a_ms: int, b_ms: int) -> bool:
    """True if lap a is strictly faster than lap b."""
    return (a_ms<b_ms)

def pace_delta_pct(a_ms,b_ms) -> int:
    """how much slower a is than b as a percentage"""
    