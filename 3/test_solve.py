import pytest
import solve

def test_part1():
    assert 0 == solve.part1('mul(4*')
    assert 0 == solve.part1('mul(6,9!')
    assert 0 == solve.part1('?(12,34)')
    assert 0 == solve.part1('mul ( 2 , 4 )')
    assert 161 == solve.part1('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')

def test_part2():
    puzzle = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert 48 == solve.part2(puzzle)
