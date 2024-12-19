import pytest
import solve

def test_solve():
    puzzle =  """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

    assert (6, 16) == solve.solve(puzzle)
