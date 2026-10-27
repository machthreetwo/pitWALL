import pytest

from pitwall.strategy import (
    PIT_LOSS_MS, Compound, Hard, Medium, OneStop, Soft, Strategy, TwoStop, best_strategy, compound_from_name,
)


def test_abstract_classes_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Compound()
    with pytest.raises(TypeError):
        Strategy()


def test_compounds():
    assert isinstance(Soft(), Compound)
    assert Medium().lap_penalty(0) == 350
    assert Hard().lap_penalty(10) == 700 + 500
    assert Soft().lap_penalty(18) == 110 * 18 + 1_500   # cliff
    assert compound_from_name("HARD").name == "hard"
    with pytest.raises(ValueError):
        compound_from_name("wet")


def test_one_stop():
    s = OneStop(Medium(), Hard(), 20)
    stints = s.stints(50)
    assert [(c.name, n) for c, n in stints] == [("medium", 20), ("hard", 30)]
    assert s.pit_laps(50) == [20]
    with pytest.raises(ValueError):
        s.stints(20)


def test_two_stop():
    s = TwoStop((Soft(), Medium(), Soft()), (15, 35))
    assert [n for _, n in s.stints(50)] == [15, 20, 15]
    assert s.pit_laps(50) == [15, 35]
    with pytest.raises(ValueError):
        TwoStop((Soft(), Soft(), Soft()), (30, 20)).stints(50)


def test_estimate_includes_pit_loss():
    s = OneStop(Soft(), Soft(), 1)
    expected = (90_000 + 0) + (90_000 + 0) + PIT_LOSS_MS
    assert s.estimate_race_ms(90_000, 2) == expected


def test_best_strategy_is_polymorphic():
    options = [
        OneStop(Soft(), Hard(), 15),
        OneStop(Medium(), Hard(), 25),
        TwoStop((Soft(), Medium(), Soft()), (16, 38)),
    ]
    best = best_strategy(options, 90_000, 55)
    assert best is min(options, key=lambda s: s.estimate_race_ms(90_000, 55))
    assert "OneStop" in repr(options[0])
