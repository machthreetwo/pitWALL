import pytest

from pitwall.analysis import add_stints, race_to_df
from pitwall.plots import plot_degradation, plot_lap_times, save_figure


def test_plot_lap_times(small_race, tmp_path):
    ax = plot_lap_times(race_to_df(small_race))
    assert len(ax.get_lines()) == 3
    assert ax.get_ylabel() == "Lap time (s)"
    path = save_figure(ax, tmp_path / "plots" / "laps.png")
    assert path.exists() and path.stat().st_size > 1000


def test_plot_degradation(small_race, tmp_path):
    df = add_stints(race_to_df(small_race), {"Lando Norris": [2]})
    ax = plot_degradation(df, "Lando Norris")
    assert "Lando Norris" in ax.get_title()
    assert len(ax.collections) == 2       # one scatter per stint
    save_figure(ax, tmp_path / "deg.png")
    with pytest.raises(ValueError):
        plot_degradation(df, "Nobody")
