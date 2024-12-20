import pytest
import solve

def test_solve():
    puzzle =  """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

    assert (14+14+2+4+2+3+1+1+1+1+1, 32+31+29+39+25+23+20+19+12+14+12+22+4+3) == solve.solve(puzzle)
