import pytest
import solve

def test_solve():
    puzzle =  """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732

"""

    assert (36, 81) == solve.solve(puzzle)
