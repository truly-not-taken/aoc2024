
def convert(sch):
    return [i.count('#')-1 for i in zip(*sch)]

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    locks = []
    keys=[]

    sch = []
    for line in puzzle.splitlines():
        if line=='':
            if sch[0]=='#####':
                locks.append(convert(sch))
            else:
                keys.append(convert(sch))
            sch = []
        else:
            sch.append(line)
    if sch:
        if sch[0]=='#####':
            locks.append(convert(sch))
        else:
            keys.append(convert(sch))

    print(len(locks))
    print(len(keys))

    answer1 = sum(all(l+k<=5 for l,k in zip(key,lock)) for lock in locks for key in keys)

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
