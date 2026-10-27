from pitwall.penalties import (
    apply_penalty_inplace, apply_time_penalty, make_grid, same_object, snapshot, swap_positions,
)


def test_apply_time_penalty_returns_new_dict():
    totals = {"VER": 100, "NOR": 105}
    result = apply_time_penalty(totals, "VER", 10)
    assert result == {"VER": 110, "NOR": 105}
    assert totals == {"VER": 100, "NOR": 105}
    assert result is not totals


def test_apply_penalty_inplace():
    totals = {"VER": 100}
    assert apply_penalty_inplace(totals, "VER", 5) is None
    assert totals == {"VER": 105}


def test_make_grid_rows_are_independent():
    grid = make_grid(3)
    grid[0][0] = "VER"
    assert grid == [["VER", None], [None, None], [None, None]]
    assert len({id(row) for row in grid}) == 3


def test_snapshot_is_deep():
    state = {"laps": {"VER": [1, 2]}, "flags": ["green"]}
    snap = snapshot(state)
    state["laps"]["VER"].append(3)
    state["flags"][0] = "red"
    assert snap == {"laps": {"VER": [1, 2]}, "flags": ["green"]}


def test_swap_positions():
    order = ["VER", "NOR", "LEC"]
    assert swap_positions(order, 0, 2) == ["LEC", "NOR", "VER"]
    assert order == ["VER", "NOR", "LEC"]


def test_same_object():
    a = [1]
    assert same_object(a, a)
    assert not same_object(a, [1])
