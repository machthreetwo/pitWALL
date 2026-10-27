import pytest

from pitwall.session import Lap, Session


def test_lap_repr_str_eq_hash():
    lap = Lap("VER", 3, 83_456)
    assert repr(lap) == "Lap('VER', 3, 83456)"
    assert str(lap) == "VER L3 1:23.456"
    assert lap == Lap("VER", 3, 83_456)
    assert len({lap, Lap("VER", 3, 83_456)}) == 1
    assert (lap == "VER") is False


def test_lap_ordering():
    laps = [Lap("A", 1, 90_200), Lap("B", 1, 90_100), Lap("C", 1, 90_300)]
    assert [lap.driver for lap in sorted(laps)] == ["B", "A", "C"]
    assert Lap("A", 1, 1) <= Lap("A", 1, 1)
    assert Lap("A", 1, 2) > Lap("A", 1, 1)


def test_lap_slots():
    with pytest.raises(AttributeError):
        Lap("A", 1, 1).colour = "red"


def test_session_protocols(small_race):
    s = Session.from_race("Monza", small_race)
    assert len(s) == 12
    assert bool(s) and not Session("empty")
    assert isinstance(s[0], Lap)
    assert len(s[1:3]) == 2
    assert [lap.number for lap in s["Lando Norris"]] == [1, 2, 3, 4]
    assert "Lando Norris" in s and "Nobody" not in s
    assert sum(1 for _ in s) == 12
    assert repr(s) == "Session('Monza', 12 laps)"


def test_session_fastest_and_drivers(small_race):
    s = Session.from_race("Monza", small_race)
    assert s.fastest() == Lap("Charles Leclerc", 3, 90_300)
    assert s.drivers() == sorted(small_race)
    with pytest.raises(ValueError):
        Session("x").fastest()


def test_session_add_operator():
    a = Session("FP1", [Lap("A", 1, 1)])
    b = Session("FP2", [Lap("B", 1, 2)])
    c = a + b
    assert c.name == "FP1+FP2" and len(c) == 2 and len(a) == 1
    with pytest.raises(TypeError):
        a + 5
