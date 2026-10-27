import random

import pytest

from pitwall.models import Car, Driver, Tyre


def test_tyre_validation_and_repr():
    t = Tyre("soft")
    assert (t.compound, t.age) == ("soft", 0)
    assert repr(t) == "Tyre('soft', age=0)"
    with pytest.raises(ValueError):
        Tyre("wet")
    with pytest.raises(ValueError):
        Tyre("soft", -1)


def test_tyre_wear_and_cliff():
    t = Tyre.used("medium", 14)
    assert isinstance(t, Tyre)
    assert t.wear == pytest.approx(0.5)
    assert not t.is_past_cliff()
    for _ in range(14):
        t.run_lap()
    assert t.is_past_cliff()


def test_class_vs_instance_attributes():
    a, b = Tyre("soft"), Tyre("hard")
    a.run_lap()
    assert (a.age, b.age) == (1, 0)
    assert a.LIFE is b.LIFE is Tyre.LIFE


def test_wear_is_read_only():
    with pytest.raises(AttributeError):
        Tyre("soft").wear = 0.1


def test_driver_code():
    assert Driver("Oscar Piastri", 90_000).code == "PIA"


def test_car_drives_ages_and_burns():
    car = Car(Driver("Lando Norris", 90_000), Tyre("soft"), fuel_kg=10.0)
    first = car.drive_lap()
    second = car.drive_lap()
    assert first == 90_000 + 10.0 * 30
    assert second == round(90_000 + 110 * 1 + 8.4 * 30)
    assert car.tyre.age == 2
    assert car.fuel_kg == pytest.approx(6.8)
    assert car.total_ms == first + second


def test_pit_stop():
    car = Car(Driver("Lando Norris", 90_000), Tyre("soft", 15), fuel_kg=0)
    car.drive_lap(noise_ms=100, rng=random.Random(0))
    before = car.laps[-1]
    car.pit("hard")
    assert car.tyre.compound == "hard" and car.tyre.age == 0
    assert car.pit_stops == 1
    assert car.laps[-1] == before + 22_000
