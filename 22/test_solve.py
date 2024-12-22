import pytest
import solve


def test_solve():
    puzzle =  """1
10
100
2024
"""

    assert (37327623, 24) == solve.solve(puzzle)

def test_2():
    puzzle =  """1
2
3
2024
"""

    assert (37990510, 23) == solve.solve(puzzle)
