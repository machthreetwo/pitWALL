# PitWall starter

The companion repo for *Python by Building: PitWall*.

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest tests/test_ch01_units.py
```

Every function raises `NotImplementedError("Chapter N: ...")`. Work through the book in order and
make each chapter's tests pass. `pytest -m "not slow"` skips the slow ML and multiprocessing tests.
