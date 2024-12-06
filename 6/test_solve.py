import pytest
import solve

# def test_part1():
    # puzzle =  """
# """
    # assert 0 == solve.part1(puzzle)

# def test_part2():
    # puzzle =  """
# """

    # assert 0 == solve.part2(puzzle)

def test_solve():
    puzzle =  """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

    assert (41, 6) == solve.solve(puzzle)
