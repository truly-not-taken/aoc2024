import pytest
import solve

def test_solve():
    puzzle =  """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

    assert ('4,6,3,5,6,3,5,2,1,0', 0) == solve.solve(puzzle)

def test_solve_1():
    puzzle =  """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
"""

    assert ('0,1,2', 0) == solve.solve(puzzle)

def test_solve_2():
    puzzle =  """Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

    assert ('4,2,5,6,7,7,7,7,3,1,0', 0) == solve.solve(puzzle)

def test_solve_3():
    puzzle =  """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

    assert ('5,7,3,0', 117440) == solve.solve(puzzle)

