# Chapter 3 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 3: control flow and loops - running a stint lap by lap."""


def tyre_life(compound: str) -> int:
    """Laps until the tyre falls off the cliff. 0 for an unknown compound."""
    match compound:
        case "soft":
            return 18
        case "medium":
            return 28
        case "hard":
            return 44
        case _:
            return 0
    


def tyre_state(age_laps: int, compound: str) -> str:
    """Classify a tyre: 'unknown', 'fresh', 'ok', 'worn' or 'cliff'.

    fresh: age <= 3; cliff: age >= life; worn: age >= 70% of life; else ok.
    """
    if tyre_life==0:
        return "unknown"
    elif age_laps<=3:
        return "fresh"
    elif age_laps>=tyre_life:
        return "cliff"
    elif age_laps>0.7*tyre_life:
        return "worn"
    else:
        return "ok"


def stint_laptimes(base_ms: int, laps: int, deg_ms_per_lap: int) -> list[int]:
    """Lap times for a stint where each lap is deg_ms_per_lap slower than the last."""
    
    


def first_lap_over(laptimes: list[int], threshold_ms: int) -> int:
    """1-based number of the first lap slower than threshold, or -1 if none."""
    raise NotImplementedError("Chapter 3: implement first_lap_over")


def laps_until_cliff(compound: str, age_laps: int) -> int:
    """Laps left before the cliff (never negative). Uses a while loop on purpose."""
    raise NotImplementedError("Chapter 3: implement laps_until_cliff")


def count_in_window(laptimes: list[int], low_ms: int, high_ms: int) -> int:
    """How many laps fall inside [low_ms, high_ms] inclusive."""
    raise NotImplementedError("Chapter 3: implement count_in_window")
