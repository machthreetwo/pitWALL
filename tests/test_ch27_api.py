import pytest
from fastapi.testclient import TestClient

from pitwall.api import create_app
from pitwall.predict import make_training_data, train_deg_model


@pytest.fixture(scope="module")
def model():
    return train_deg_model(make_training_data(800))[0]


@pytest.fixture
def client(model):
    return TestClient(create_app(model=model))


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_create_race_and_standings(client):
    r = client.post("/races", json={"name": "Monza", "laps": 5, "seed": 1})
    assert r.status_code == 201
    body = r.json()
    assert body["name"] == "Monza" and len(body["standings"]) == 6
    assert body["standings"][0]["gap_ms"] == 0 and body["standings"][0]["position"] == 1

    rid = body["race_id"]
    again = client.get(f"/races/{rid}/standings")
    assert again.status_code == 200 and again.json() == body["standings"]
    fastest = client.get(f"/races/{rid}/fastest").json()
    assert fastest == sorted(fastest, key=lambda row: row["best_ms"])


def test_custom_drivers(client):
    r = client.post("/races", json={"name": "Duel", "laps": 3, "seed": 1, "noise_ms": 0,
                                    "drivers": {"Fast Driver": 89_000, "Slow Driver": 91_000}})
    rows = r.json()["standings"]
    assert [row["driver"] for row in rows] == ["Fast Driver", "Slow Driver"]
    assert rows[1]["gap_ms"] == 6_000


def test_validation_errors(client):
    assert client.post("/races", json={"name": "X", "laps": 0}).status_code == 422
    assert client.post("/races", json={"laps": 5}).status_code == 422
    assert client.post("/predict", json={"compound": "wet", "tyre_age": 1, "fuel_kg": 1, "track_temp": 30}).status_code == 422


def test_conflict_and_not_found(client):
    client.post("/races", json={"name": "Spa", "laps": 2})
    assert client.post("/races", json={"name": "Spa", "laps": 2}).status_code == 409
    assert client.get("/races/999/standings").status_code == 404


def test_predict(client):
    r = client.post("/predict", json={"compound": "soft", "tyre_age": 25, "fuel_kg": 40, "track_temp": 40})
    assert r.status_code == 200
    assert r.json()["lap_delta_ms"] > 2000
