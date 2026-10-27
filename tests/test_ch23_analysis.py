import numpy as np
import pandas as pd
import pytest

from pitwall.analysis import (
    add_stints, array_to_df, drop_slow_laps, merge_driver_info, pace_table, race_to_df, rolling_pace, stint_summary,
)


def test_race_to_df(small_race):
    df = race_to_df(small_race)
    assert list(df.columns) == ["driver", "lap", "lap_ms", "lap_s"]
    assert len(df) == 12
    assert df.loc[(df.driver == "Lando Norris") & (df.lap == 2), "lap_s"].item() == pytest.approx(90.4)


def test_array_to_df_matches_dict_version():
    times = np.array([[90_000.4, 90_100.0], [91_000.0, 90_900.0]])
    df = array_to_df(times, ["B", "A"])
    assert df[["driver", "lap", "lap_ms"]].values.tolist() == [["A", 1, 91_000], ["A", 2, 90_900],
                                                               ["B", 1, 90_000], ["B", 2, 90_100]]


def test_add_stints_does_not_mutate():
    df = race_to_df({"A": [1] * 5, "B": [1] * 5})
    out = add_stints(df, {"A": [2, 4]})
    assert "stint" not in df
    assert out[out.driver == "A"]["stint"].tolist() == [1, 1, 2, 2, 3]
    assert out[out.driver == "B"]["stint"].tolist() == [1] * 5


def test_drop_slow_laps():
    df = race_to_df({"A": [90_000, 90_100, 112_000, 90_200]})
    assert drop_slow_laps(df)["lap_ms"].tolist() == [90_000, 90_100, 90_200]


def test_stint_summary():
    df = add_stints(race_to_df({"A": [90_000, 90_100, 90_200, 89_000, 89_050]}), {"A": [3]})
    s = stint_summary(df).set_index("stint")
    assert s.loc[1, "laps"] == 3 and s.loc[2, "laps"] == 2
    assert s.loc[1, "best_ms"] == 90_000
    assert s.loc[1, "deg_ms_per_lap"] == pytest.approx(100)
    assert s.loc[2, "deg_ms_per_lap"] == pytest.approx(50)


def test_pace_table(small_race):
    wide = pace_table(race_to_df(small_race))
    assert wide.shape == (3, 4)
    assert wide.loc["Charles Leclerc", 3] == 90_300


def test_rolling_pace_never_mixes_drivers():
    df = race_to_df({"A": [10, 20, 30], "B": [1000, 2000, 3000]})
    r = rolling_pace(df, window=2)
    assert r.isna().sum() == 2
    assert r.dropna().tolist() == [15.0, 25.0, 1500.0, 2500.0]


def test_merge_driver_info(small_race):
    info = pd.DataFrame({"driver": ["Lando Norris", "Max Verstappen"], "team": ["McLaren", "Red Bull"]})
    merged = merge_driver_info(race_to_df(small_race), info)
    assert len(merged) == 12
    assert merged["team"].isna().sum() == 4   # Leclerc has no info -> NaN, not dropped
    dupes = pd.concat([info, info])
    with pytest.raises(pd.errors.MergeError):
        merge_driver_info(race_to_df(small_race), dupes)
