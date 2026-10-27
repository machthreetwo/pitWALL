"""Shared fixtures. pytest finds this file automatically (Chapter 19)."""

import pytest


@pytest.fixture
def small_race() -> dict[str, list[int]]:
    """Three drivers, four laps, hand-written so every answer is checkable by hand."""
    return {
        "Max Verstappen": [91_000, 90_500, 90_600, 90_700],   # total 362_800
        "Lando Norris":   [91_200, 90_400, 90_450, 90_500],   # total 362_550 (winner)
        "Charles Leclerc": [91_500, 90_900, 90_300, 91_000],  # total 363_700, fastest lap 90_300 on L3
    }
