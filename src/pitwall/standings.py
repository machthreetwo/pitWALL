# Chapter 5 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 5: lists, tuples, dicts, sets and comprehensions - standings."""

Race = dict[str, list[int]]


def total_times(race: Race) -> dict[str, int]:
    """Total race time per driver."""
    raise NotImplementedError("Chapter 5: implement total_times")


def classify(race: Race) -> list[tuple[int, str, int]]:
    """Final classification as (position, driver, total_ms), fastest first.

    Ties are broken alphabetically by driver name so output is deterministic.
    """
    raise NotImplementedError("Chapter 5: implement classify")


def gaps_to_leader(classification: list[tuple[int, str, int]]) -> dict[str, int]:
    """Gap in ms from each driver to the winner (winner's gap is 0)."""
    raise NotImplementedError("Chapter 5: implement gaps_to_leader")


def fastest_lap(race: Race) -> tuple[str, int, int]:
    """(driver, 1-based lap number, lap_ms) of the single fastest lap."""
    raise NotImplementedError("Chapter 5: implement fastest_lap")


def compounds_used(stints: list[tuple[str, str]]) -> dict[str, set[str]]:
    """From (driver, compound) pairs, the set of compounds each driver used."""
    raise NotImplementedError("Chapter 5: implement compounds_used")


def lap_leaders(race: Race) -> list[str]:
    """Who led (lowest cumulative time) at the end of each lap."""
    raise NotImplementedError("Chapter 5: implement lap_leaders")


def position_changes(start_grid: list[str], classification: list[tuple[int, str, int]]) -> dict[str, int]:
    """Places gained (+) or lost (-) from grid slot to finishing position."""
    raise NotImplementedError("Chapter 5: implement position_changes")
