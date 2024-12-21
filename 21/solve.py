
import itertools

def numeric(code):
    keypad = {
        'AA':'A',
        'A0':'<A',
        'A1':'^<<A',
        'A2':'^<A',
        'A3':'^A',
        'A4':'^^<<A',
        'A5':'^^<A',
        'A6':'^^A',
        'A7':'^^^<<A',
        'A8':'^^^<A',
        'A9':'^^^A',

        '0A':'>A',
        '00':'A',
        '01':'^<A',
        '02':'^A',
        '03':'>^A',
        '04':'^^<A',
        '05':'^^A',
        '06':'>^^A',
        '07':'^^^<A',
        '08':'^^^A',
        '09':'>^^^A',

        '1A':'>>vA',
        '10':'>vA',
        '11':'A',
        '12':'>A',
        '13':'>>A',
        '14':'^A',
        '15':'>^A',
        '16':'>>^A',
        '17':'^^A',
        '18':'>^^A',
        '19':'>>^^A',

        '2A':'>vA',
        '20':'vA',
        '21':'<A',
        '22':'A',
        '23':'>A',
        '24':'^<A',
        '25':'^A',
        '26':'>^A',
        '27':'^^<A',
        '28':'^^A',
        '29':'>^^A',

        '3A':'vA',
        '30':'v<A',
        '31':'<<A',
        '32':'<A',
        '33':'A',
        '34':'^<<A',
        '35':'^<A',
        '36':'^A',
        '37':'<<^^A',
        '38':'^^<A',
        '39':'^^A',

        '4A':'>>vvA',
        '40':'>vvA',
        '41':'vA',
        '42':'>vA',
        '43':'>>vA',
        '44':'A',
        '45':'>A',
        '46':'>>A',
        '47':'^A',
        '48':'>^A',
        '49':'>>^A',

        '5A':'>vvA',
        '50':'vvA',
        '51':'v<A',
        '52':'vA',
        '53':'>vA',
        '54':'<A',
        '55':'A',
        '56':'>A',
        '57':'^<A',
        '58':'^A',
        '59':'>^A',

        '6A':'vvA',
        '60':'vv<A',
        '61':'v<<A',
        '62':'v<A',
        '63':'vA',
        '64':'<<A',
        '65':'<A',
        '66':'A',
        '67':'^<<A',
        '68':'^<A',
        '69':'^A',

        '7A':'>>vvvA',
        '70':'>vvvA',
        '71':'vvA',
        '72':'>vvA',
        '73':'>>vvA',
        '74':'vA',
        '75':'>vA',
        '76':'>>vA',
        '77':'A',
        '78':'>A',
        '79':'>>A',

        '8A':'>vvvA',
        '80':'vvvA',
        '81':'vv<A',
        '82':'vvA',
        '83':'>vvA',
        '84':'v<A',
        '85':'vA',
        '86':'>vA',
        '87':'<A',
        '88':'A',
        '89':'>A',

        '9A':'vvvA',
        '90':'vvv<A',
        '91':'vv<<A',
        '92':'vv<A',
        '93':'vvA',
        '94':'v<<A',
        '95':'v<A',
        '96':'vA',
        '97':'<<A',
        '98':'<A',
        '99':'A',
    }

    return ''.join(keypad[''.join(i)] for i in zip('A'+code, code))


def directional(code):
    keypad = {
        'AA':'A',
        'A^':'<A',
        'A<':'v<<A',
        'Av':'v<A',
        'A>':'vA',

        '^A':'>A',
        '^^':'A',
        '^<':'v<A',
        '^v':'vA',
        '^>':'>vA',

        '<A':'>>^A',
        '<^':'>^A',
        '<<':'A',
        '<v':'>A',
        '<>':'>>A',

        'vA':'>^A',
        'v^':'^A',
        'v<':'<A',
        'vv':'A',
        'v>':'>A',

        '>A':'^A',
        '>^':'^<A',
        '><':'<<A',
        '>v':'<A',
        '>>':'A',
    }

    return ''.join(keypad[''.join(i)] for i in zip('A'+code, code))


def solve(puzzle):
    answer1 = 0
    answer2 = 0

    n_kp = {
        'AA':'A',
        'A0':'<A',
        'A1':'^<<A',
        'A2':'^<A',
        'A3':'^A',
        'A4':'^^<<A',
        'A5':'^^<A',
        'A6':'^^A',
        'A7':'^^^<<A',
        'A8':'^^^<A',
        'A9':'^^^A',

        '0A':'>A',
        '00':'A',
        '01':'^<A',
        '02':'^A',
        '03':'>^A',
        '04':'^^<A',
        '05':'^^A',
        '06':'>^^A',
        '07':'^^^<A',
        '08':'^^^A',
        '09':'>^^^A',

        '1A':'>>vA',
        '10':'>vA',
        '11':'A',
        '12':'>A',
        '13':'>>A',
        '14':'^A',
        '15':'>^A',
        '16':'>>^A',
        '17':'^^A',
        '18':'>^^A',
        '19':'>>^^A',

        '2A':'>vA',
        '20':'vA',
        '21':'<A',
        '22':'A',
        '23':'>A',
        '24':'^<A',
        '25':'^A',
        '26':'>^A',
        '27':'^^<A',
        '28':'^^A',
        '29':'>^^A',

        '3A':'vA',
        '30':'v<A',
        '31':'<<A',
        '32':'<A',
        '33':'A',
        '34':'^<<A',
        '35':'^<A',
        '36':'^A',
        '37':'<<^^A',
        '38':'^^<A',
        '39':'^^A',

        '4A':'>>vvA',
        '40':'>vvA',
        '41':'vA',
        '42':'>vA',
        '43':'>>vA',
        '44':'A',
        '45':'>A',
        '46':'>>A',
        '47':'^A',
        '48':'>^A',
        '49':'>>^A',

        '5A':'>vvA',
        '50':'vvA',
        '51':'v<A',
        '52':'vA',
        '53':'>vA',
        '54':'<A',
        '55':'A',
        '56':'>A',
        '57':'^<A',
        '58':'^A',
        '59':'>^A',

        '6A':'vvA',
        '60':'vv<A',
        '61':'v<<A',
        '62':'v<A',
        '63':'vA',
        '64':'<<A',
        '65':'<A',
        '66':'A',
        '67':'^<<A',
        '68':'^<A',
        '69':'^A',

        '7A':'>>vvvA',
        '70':'>vvvA',
        '71':'vvA',
        '72':'>vvA',
        '73':'>>vvA',
        '74':'vA',
        '75':'>vA',
        '76':'>>vA',
        '77':'A',
        '78':'>A',
        '79':'>>A',

        '8A':'>vvvA',
        '80':'vvvA',
        '81':'vv<A',
        '82':'vvA',
        '83':'>vvA',
        '84':'v<A',
        '85':'vA',
        '86':'>vA',
        '87':'<A',
        '88':'A',
        '89':'>A',

        '9A':'vvvA',
        '90':'vvv<A',
        '91':'vv<<A',
        '92':'vv<A',
        '93':'vvA',
        '94':'v<<A',
        '95':'v<A',
        '96':'vA',
        '97':'<<A',
        '98':'<A',
        '99':'A',
    }

    n_kp = {
        k:tuple(''.join(i)+'A'
            for i in set(itertools.permutations(v[:-1]))
            if not (
                k[0]=='0' and i[:1]==tuple('<') or
                k[0]=='A' and i[:2]==tuple('<<') or
                k[0]=='1' and i[:1]==tuple('v') or
                k[0]=='4' and i[:2]==tuple('vv') or
                k[0]=='7' and i[:3]==tuple('vvv')
            )
        )
        for k,v in n_kp.items()
    }
    # print(n_kp)

    a_kp = {
        'AA':'A',
        'A^':'<A',
        'A<':'v<<A',
        'Av':'v<A',
        'A>':'vA',

        '^A':'>A',
        '^^':'A',
        '^<':'v<A',
        '^v':'vA',
        '^>':'>vA',

        '<A':'>>^A',
        '<^':'>^A',
        '<<':'A',
        '<v':'>A',
        '<>':'>>A',

        'vA':'>^A',
        'v^':'^A',
        'v<':'<A',
        'vv':'A',
        'v>':'>A',

        '>A':'^A',
        '>^':'^<A',
        '><':'<<A',
        '>v':'<A',
        '>>':'A',
    }
    a_kp = {
        k:tuple(''.join(i)+'A'
            for i in set(itertools.permutations(v[:-1]))
            if not (
                k[0]=='^' and i[:1]==tuple('<') or
                k[0]=='A' and i[:2]==tuple('<<') or
                k[0]=='<' and i[:1]==tuple('^')
            )
        )
        for k,v in a_kp.items()
    }
    print(a_kp)

    a_a_kp = {
        k:tuple(
            ''.join(p)
            for c in v for p in itertools.product(*(
                a_kp[''.join(i)] for i in zip('A'+c, c)
            ))
        )
        for k,v in a_kp.items()
    }
    print(a_a_kp)
    for k in a_a_kp:
        l = min(len(c) for c in a_a_kp[k])
        a_a_kp[k] = tuple(c for c in a_a_kp[k] if len(c)==l)
    print(a_a_kp)

    n_a_a_kp = {
        k:tuple(
            ''.join(p)
            for c in v for p in itertools.product(*(
                a_a_kp[''.join(i)] for i in zip('A'+c, c)
            ))
        )
        for k,v in n_kp.items()
    }
    print(n_a_a_kp)
    for k in n_a_a_kp:
        l = min(len(c) for c in n_a_a_kp[k])
        n_a_a_kp[k] = tuple(c for c in n_a_a_kp[k] if len(c)==l)
    print(n_a_a_kp)

    for code in puzzle.splitlines():
        print(code)
        # n = numeric(code)
        # print(n)
        # d1 = directional(n)
        # print(d1)
        # d2 = directional(d1)
        # print(d2,len(d2))

        # complexity = len(d2) * int(code[:-1])

        # for i in zip('A'+code, code):
            # for code2 in n_kp[''.join(i)]:
                # print(code2)
                # for j in zip('A'+code2, code2):
                    # for code3 in a_kp[''.join(j)]:
                        # print(code3)
                        # print(*(''.join(p) for p in itertools.product(*(
                            # a_kp[''.join(k)] for k in zip('A'+code3, code3))
                        # )))

        complexity = sum(min(len(c) for c in n_a_a_kp[''.join(i)]) for i in zip('A'+code, code)) * int(code[:-1])

        # continue

        # code2 = tuple(''.join(p) for p in itertools.product(*(
            # n_kp[''.join(i)] for i in zip('A'+code, code)
        # )))
        # print(code2, set(len(c) for c in code2))
        # code3 = tuple(''.join(p) for c in code2 for p in itertools.product(*(
            # a_kp[''.join(i)] for i in zip('A'+c, c)
        # )))
        # print(code3[0],len(code3), set(len(c) for c in code3))
        # code4 = tuple(''.join(p) for c in code3 for p in itertools.product(*(
            # a_kp[''.join(i)] for i in zip('A'+c, c)
        # )))
        # print(code4[0],len(code4), set(len(c) for c in code4))

        # complexity = min(len(c) for c in code4) * int(code[:-1])

        print(complexity)

        answer1 += complexity


    # not 144536
    # not 151012

    return answer1, answer2


def main():
    filename = 'input.txt'
    import sys
    if len(sys.argv)>1:
        filename = sys.argv[1]
    with open(filename) as file:
        puzzle = file.read()
        print(*solve(puzzle),sep='\n')

if __name__ == '__main__':
    main()
