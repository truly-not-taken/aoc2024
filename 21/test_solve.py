import pytest
import solve


def test_solve():
    puzzle =  """029A
980A
179A
456A
379A
"""

    assert (126384, 154115708116294) == solve.solve(puzzle)
