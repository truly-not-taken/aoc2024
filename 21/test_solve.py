import pytest
import solve


def test_numeric():
    return
    keypad = (
        ('7','8','9',),
        ('4','5','6',),
        ('1','2','3',),
        (None,'0','A',),
    )
    keys = 'A0123456789'
    for a in keys:
        s = solve.numeric(a)
        x = 2-s.count('<')+s.count('>')
        y = 3-s.count('^')+s.count('v')
        assert a == keypad[y][x]

        for b in keys:
            s = solve.numeric(a+b)
            x = 2-s.count('<')+s.count('>')
            y = 3-s.count('^')+s.count('v')
            assert b == keypad[y][x], f'{a}{b} {s}'

    for i in range(1,4):
        code = '379A'[:i]
        s = solve.numeric(code)
        x = 2-s.count('<')+s.count('>')
        y = 3-s.count('^')+s.count('v')
        assert code[-1] == keypad[y][x]

def test_directional():
    return
    keypad = (
        (None,'^','A',),
        ('<','v','>',),
    )
    keys = 'A^<v>'
    for a in keys:
        s = solve.directional(a)
        x = 2-s.count('<')+s.count('>')
        y = 0-s.count('^')+s.count('v')
        assert a == keypad[y][x]

        for b in keys:
            s = solve.directional(a+b)
            x = 2-s.count('<')+s.count('>')
            y = 0-s.count('^')+s.count('v')
            assert b == keypad[y][x]

    n = solve.numeric('379A')
    for i in range(1,4):
        code = n[:i]
        s = solve.directional(code)
        x = 2-s.count('<')+s.count('>')
        y = 0-s.count('^')+s.count('v')
        assert code[-1] == keypad[y][x]

    n = solve.directional(n)
    for i in range(1,4):
        code = n[:i]
        s = solve.directional(code)
        x = 2-s.count('<')+s.count('>')
        y = 0-s.count('^')+s.count('v')
        assert code[-1] == keypad[y][x]

# def test_1():
    # assert '<A^A>^^AvvvA' == solve.numeric('029A')
# def test_2():
    # assert 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A' == solve.directional(solve.numeric('029A'))
# def test_3():
    # assert '<vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A' == solve.directional(solve.directional(solve.numeric('029A')))


def test_solve():
    puzzle =  """029A
980A
179A
456A
379A
"""

    assert (126384, 0) == solve.solve(puzzle)
