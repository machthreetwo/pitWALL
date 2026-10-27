# Chapter 6 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 6: mutability, references and the memory model."""

import copy


def apply_time_penalty(totals: dict[str, int], driver: str, penalty_ms: int) -> dict[str, int]:
    """Return a NEW dict with the penalty added. The input must not change."""
    raise NotImplementedError("Chapter 6: implement apply_time_penalty")


def apply_penalty_inplace(totals: dict[str, int], driver: str, penalty_ms: int) -> None:
    """Mutate totals in place. Returns None, like list.sort()."""
    raise NotImplementedError("Chapter 6: implement apply_penalty_inplace")


def make_grid(rows: int, cols: int = 2) -> list[list[str | None]]:
    """A rows x cols grid of empty slots where every row is an independent list.

    [[None] * cols] * rows would repeat ONE row object `rows` times.
    """
    raise NotImplementedError("Chapter 6: implement make_grid")


def snapshot(state: dict) -> dict:
    """A fully independent copy of nested race state."""
    raise NotImplementedError("Chapter 6: implement snapshot")


def swap_positions(order: list[str], i: int, j: int) -> list[str]:
    """New running order with positions i and j (0-based) swapped."""
    raise NotImplementedError("Chapter 6: implement swap_positions")


def same_object(a: object, b: object) -> bool:
    """Identity, not equality."""
    raise NotImplementedError("Chapter 6: implement same_object")
