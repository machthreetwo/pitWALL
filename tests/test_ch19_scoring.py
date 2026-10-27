"""Chapter 19: YOU write these tests. scoring.py is already implemented.

Cover (see the chapter for detail):
  1. points_for for scoring and non-scoring positions (parametrize)
  2. points_for raises ValueError for 0 and negatives (match=)
  3. the points table sums to 101
  4. a three-race season fixture: correct leader and order
  5. equal points + equal wins -> alphabetical
  6. equal points, more wins ranks higher even when the name sorts later
  7. empty seasons: [] and [[]]
  8. championship does not mutate its input
Then mutation-test yourself: break scoring.py on purpose and check a test fails.
"""

import pytest

from pitwall.scoring import POINTS, championship, points_for


def test_winner_scores_25():
    assert points_for(1) == 25


# TODO: your tests here
