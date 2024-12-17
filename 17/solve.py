
import math

def execute(a,b,c,program):
    ip = 0

    out = []
    while ip in range(len(program)):
        opcode = program[ip]
        literal = program[ip+1]
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}[literal]

        # print('a',a,'b',b,'c',c,'ip',ip,'opcode',opcode,'literal',literal,'combo',combo,out)

        if opcode == 0:
            a = math.trunc(a/(2**combo))
            ip += 2
        elif opcode == 1:
            b = b ^ literal
            ip += 2
        elif opcode == 2:
            b = combo % 8
            ip += 2
        elif opcode == 3:
            if a!=0:
                ip = literal
            else:
                ip += 2
        elif opcode == 4:
            b = b ^ c
            ip += 2
        elif opcode == 5:
            out.append(combo % 8)
            ip += 2
        elif opcode == 6:
            b = math.trunc(a/(2**combo))
            ip += 2
        elif opcode == 7:
            c = math.trunc(a/(2**combo))
            ip += 2
    return out

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    data = puzzle.splitlines()
    a = int(data[0].split()[2])
    b = int(data[1].split()[2])
    c = int(data[2].split()[2])

    program = [int(i) for i in data[4].split()[1].split(',')]

    out = execute(a,b,c,program)

    answer1 = ','.join(str(i) for i in out)

    # assume a is divided by 8 in the loop
    # assume b and c are erased in each iteration
    a = [0]
    for i in reversed(range(len(program))):
        a = [j*8+k for j in a for k in range(8) if execute(j*8+k,0,0,program) == program[i:]]
    answer2 = min(a,default=0)

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
