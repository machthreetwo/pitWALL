# Chapter 19 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 19: pytest - the module YOU write tests for.

Championship points. Top 10 score 25-18-15-12-10-8-6-4-2-1.
"""

POINTS = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)


def points_for(position: int) -> int:
    """Points for a finishing position (1-based). Outside the top 10 scores 0."""
    if position < 1:
        raise ValueError("position must be >= 1")
    return POINTS[position - 1] if position <= len(POINTS) else 0


def championship(results: list[list[str]]) -> list[tuple[str, int]]:
    """Standings from several races, each given as a finishing order.

    Sorted by points (high first); ties broken by number of wins, then name.
    """
    points: dict[str, int] = {}
    wins: dict[str, int] = {}
    for order in results:
        for pos, driver in enumerate(order, start=1):
            points[driver] = points.get(driver, 0) + points_for(pos)
            wins.setdefault(driver, 0)
        if order:
            wins[order[0]] += 1
    return sorted(points.items(), key=lambda kv: (-kv[1], -wins[kv[0]], kv[0]))
