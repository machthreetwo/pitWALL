# Chapter 15 - see the book. Replace each NotImplementedError with a real body.
"""Chapter 15: dataclasses, type hints and Protocols - typed telemetry."""

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Literal, Protocol, runtime_checkable

CompoundName = Literal["soft", "medium", "hard"]


@dataclass(frozen=True, slots=True)
class Sample:
    """One telemetry reading. Frozen: once recorded, it never changes."""

    t_ms: int
    speed_kmh: float
    throttle: float
    brake: bool
    gear: int

    def __post_init__(self):
        raise NotImplementedError("Chapter 15: implement __post_init__")


@dataclass
class StintRecord:
    driver: str
    compound: CompoundName
    laps: list[int] = field(default_factory=list)

    @property
    def avg_ms(self) -> float:
        raise NotImplementedError("Chapter 15: implement avg_ms")

    def add(self, lap_ms: int) -> None:
        raise NotImplementedError("Chapter 15: implement add")


@runtime_checkable
class TelemetrySource(Protocol):
    """Anything with a .read() that yields Samples. No inheritance required."""

    def read(self) -> Iterable[Sample]: ...


class ListSource:
    """A TelemetrySource backed by a list. Note: it does NOT subclass TelemetrySource."""

    def __init__(self, samples: list[Sample]):
        raise NotImplementedError("Chapter 15: implement __init__")

    def read(self) -> Iterable[Sample]:
        raise NotImplementedError("Chapter 15: implement read")


def max_speed(source: TelemetrySource) -> float:
    """Top speed from any source that satisfies the protocol."""
    raise NotImplementedError("Chapter 15: implement max_speed")


def full_throttle_ratio(source: TelemetrySource) -> float:
    """Fraction of samples at >= 99% throttle."""
    raise NotImplementedError("Chapter 15: implement full_throttle_ratio")
