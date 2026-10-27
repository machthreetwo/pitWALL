import pytest

from pitwall.predict import (
    FEATURES, TARGET, build_pipeline, load_model, make_training_data, predict_lap_delta, save_model, train_deg_model,
)


@pytest.fixture(scope="module")
def data():
    return make_training_data(2000, seed=0)


@pytest.fixture(scope="module")
def forest(data):
    return train_deg_model(data)


def test_training_data(data):
    assert list(data.columns) == FEATURES + [TARGET]
    assert set(data["compound"]) == {"soft", "medium", "hard"}
    assert make_training_data(10, seed=1).equals(make_training_data(10, seed=1))


@pytest.mark.slow
def test_forest_beats_linear(data, forest):
    _, forest_metrics = forest
    _, linear_metrics = train_deg_model(data, kind="linear")
    assert forest_metrics["r2"] > 0.95
    assert forest_metrics["mae_ms"] < linear_metrics["mae_ms"]


def test_predictions_make_physical_sense(forest):
    model, _ = forest
    fresh = predict_lap_delta(model, "soft", 2, 50, 35)
    old = predict_lap_delta(model, "soft", 25, 50, 35)
    assert old > fresh + 1000          # past the cliff it is much slower
    assert predict_lap_delta(model, "hard", 10, 50, 35) > predict_lap_delta(model, "soft", 2, 50, 35)


def test_save_and_load(forest, tmp_path):
    model, _ = forest
    path = save_model(model, tmp_path / "m" / "deg.joblib")
    again = load_model(path)
    # approx, not ==: parallel trees can sum in a different order -> last-bit float differences
    assert predict_lap_delta(again, "medium", 10, 30, 30) == pytest.approx(predict_lap_delta(model, "medium", 10, 30, 30))


def test_unknown_kind():
    with pytest.raises(ValueError):
        build_pipeline("svm")
