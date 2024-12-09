import pytest
import solve

def test_solve():
    puzzle =  """2333133121414131402
"""

    assert (1928, 2858) == solve.solve(puzzle)
