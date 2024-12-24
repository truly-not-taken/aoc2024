
def solve(puzzle):
    answer1 = 0
    answer2 = 0

    lines = puzzle.splitlines()
    split = lines.index('')

    wires = {}
    for line in lines[:split]:
        k,v = line.split(': ')
        wires[k] = int(v)
    # print(wires)
    gates = {}
    for line in lines[split+1:]:
        in1, op, in2, _, out = line.split()
        if in1>in2:
            in1, in2 = in2, in1
        gates[out] = (op, in1, in2)
    # print(gates)

    missed = True
    while missed:
        missed = False
        for out, (op, in1, in2) in gates.items():
            if out not in wires:
                if  in1 in wires and in2 in wires:
                    if op == 'AND':
                        v = int(wires[in1] and wires[in2])
                    elif op == 'OR':
                        v = int(wires[in1] or wires[in2])
                    elif op == 'XOR':
                        v = int(wires[in1] != wires[in2])
                    else:
                        return 'error'
                    wires[out] = v
                else:
                    missed = True
    # print(wires)
    z = [(k,v) for k,v in wires.items() if k[0]=='z']
    z.sort()
    # print(z)
    bits = [v for k,v in z]
    # print(bits)
    answer1 = sum((2**i)*bit for i,bit in enumerate(bits))

    def unroll(out):
        if out[0] in 'xy':
            return out
        else:
            op, in1, in2 = gates[out]
            return (unroll(in1), op, unroll(in2))

    def count(out):
        if out[0] in 'xy':
            return 1
        else:
            op, in1, in2 = gates[out]
            return count(in1) + count(in2)

    print(len(z))

    # z20, msn, cqr
    # z15, rjm, qnw
    # z37, dnt, vkg

    gates['z20'], gates['cqr'] = gates['cqr'], gates['z20']
    gates['z15'], gates['qnw'] = gates['qnw'], gates['z15']
    gates['z37'], gates['vkg'] = gates['vkg'], gates['z37']
    gates['ncd'], gates['nfj'] = gates['nfj'], gates['ncd']

    short = [(in1[1:],out) for out,(op, in1, in2) in gates.items() if op=='XOR' and in1[0] in 'xy' and in2[0] in 'xy']
    short.sort()
    short = {v:k for k,v in short}
    print(short, len(short))

    final = [(out, (in1 if in1 in short else in2)) for out,(op, in1, in2) in gates.items() if op=='XOR' and (in1 in short or in2 in short)]
    final.sort()
    final=dict(final)
    print(final,len(final))

    print([k for k in short.keys() if k not in final.values()])

    for k in ['z20','cqr', 'msn', 'z15','qnw', 'rjm', 'z37','vkg', 'dnt', 'ncd', 'z27', 'nfj']:
        print(k,gates[k], unroll(k))
        print()

    for out,_ in z[1:3]:
        print(out, unroll(out))
        in1 = 'x'+out[1:]
        in2 = 'y'+out[1:]
        print(f'({in1} xor {in2}) xor (something long)')

    answer2 = ','.join(sorted(['z20','cqr','z15','qnw','z37','vkg','ncd','nfj']))

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
