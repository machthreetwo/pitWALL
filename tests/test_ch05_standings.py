from pitwall.standings import (
    classify, compounds_used, fastest_lap, gaps_to_leader, lap_leaders, position_changes, total_times,
)


def test_total_times(small_race):
    assert total_times(small_race)["Lando Norris"] == 362_550


def test_classify(small_race):
    table = classify(small_race)
    assert [d for _, d, _ in table] == ["Lando Norris", "Max Verstappen", "Charles Leclerc"]
    assert table[0] == (1, "Lando Norris", 362_550)


def test_classify_tie_breaks_alphabetically():
    table = classify({"B": [100], "A": [100]})
    assert [d for _, d, _ in table] == ["A", "B"]


def test_gaps(small_race):
    gaps = gaps_to_leader(classify(small_race))
    assert gaps == {"Lando Norris": 0, "Max Verstappen": 250, "Charles Leclerc": 1_150}
    assert gaps_to_leader([]) == {}


def test_fastest_lap(small_race):
    assert fastest_lap(small_race) == ("Charles Leclerc", 3, 90_300)


def test_compounds_used():
    used = compounds_used([("VER", "medium"), ("VER", "hard"), ("NOR", "medium"), ("VER", "medium")])
    assert used == {"VER": {"medium", "hard"}, "NOR": {"medium"}}


def test_lap_leaders(small_race):
    # after L1: VER 91000 leads; after L2: VER 181500 vs NOR 181600; after L3: NOR 272050 vs VER 272100
    assert lap_leaders(small_race) == ["Max Verstappen", "Max Verstappen", "Lando Norris", "Lando Norris"]


def test_position_changes(small_race):
    grid = ["Charles Leclerc", "Max Verstappen", "Lando Norris"]
    changes = position_changes(grid, classify(small_race))
    assert changes == {"Lando Norris": 2, "Max Verstappen": 0, "Charles Leclerc": -2}
