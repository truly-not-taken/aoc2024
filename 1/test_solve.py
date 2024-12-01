import pytest
import solve

def test_part1():
    puzzle = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3'
    assert 11 == solve.part1(puzzle)

def test_part2():
    puzzle = '3   4\n4   3\n2   5\n1   3\n3   9\n3   3'
    assert 31 == solve.part2(puzzle)
