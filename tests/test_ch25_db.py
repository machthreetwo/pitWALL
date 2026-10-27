import sqlite3

import pytest

from pitwall.db import RaceDB


@pytest.fixture
def db():
    with RaceDB() as database:
        yield database


def test_insert_and_query(db, small_race):
    rid = db.insert_race("Monza", small_race)
    assert db.race_id("Monza") == rid
    assert db.race_id("Spa") is None
    assert db.fastest_laps(rid)[0] == ("Charles Leclerc", 90_300)
    assert db.classification(rid)[0] == ("Lando Norris", 4, 362_550)


def test_duplicate_name_rolls_back(db, small_race):
    db.insert_race("Monza", small_race)
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_race("Monza", small_race)
    assert db.conn.execute("SELECT COUNT(*) FROM laps").fetchone()[0] == 12


def test_transaction_is_atomic(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_race("Bad", {"A": [90_000], None: [90_100]})   # NULL driver violates NOT NULL
    assert db.race_id("Bad") is None


def test_injection_is_harmless(db, small_race):
    db.insert_race("Monza", small_race)
    assert db.race_id("x' OR '1'='1") is None


def test_laps_df_and_cascade(db, small_race):
    rid = db.insert_race("Monza", small_race)
    df = db.laps_df(rid)
    assert list(df.columns) == ["driver", "lap", "lap_ms"] and len(df) == 12
    db.delete_race(rid)
    assert db.conn.execute("SELECT COUNT(*) FROM laps").fetchone()[0] == 0


def test_persists_to_disk(tmp_path, small_race):
    path = tmp_path / "pitwall.db"
    with RaceDB(path) as a:
        a.insert_race("Monza", small_race)
    with RaceDB(path) as b:
        assert b.race_id("Monza") is not None
