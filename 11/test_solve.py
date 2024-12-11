import pytest
import solve

def test_blink():
    puzzle = [0, 1, 10, 99, 999]
    assert [1, 2024, 1, 0, 9, 9, 2021976] == solve.blink(puzzle)

    assert [253000, 1, 7] == solve.blink([125, 17])

def test_blink2():
    puzzle = [0, 1, 10, 99, 999]
    assert len([1, 2024, 1, 0, 9, 9, 2021976]) == sum(solve.blink2(i,1) for i in puzzle)

    assert len([253000, 1, 7]) == sum(solve.blink2(i,1) for i in [125, 17])

    assert 22 == sum(solve.blink2(i,6) for i in [125, 17])

def test_solve():
    puzzle =  """125 17
"""

    assert (55312, 65601038650482) == solve.solve(puzzle)

