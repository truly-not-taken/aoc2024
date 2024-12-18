
def solve(puzzle, fallen=1024):
    answer1 = 0
    answer2 = 0

    incoming = [tuple(int(i) for i in line.split(',')) for line in puzzle.splitlines()]

    n = 1 + max(j for i in incoming for j in i)

    safe = [[True for i in range(n)] for j in range(n)]

    for x,y in incoming[:fallen]:
        safe[y][x] = False

    # print('\n'.join(''.join('.' if s else '#' for s in line) for line in safe))
    # print()

    distance = [[(0,0)]]
    safe[0][0] = False
    e = (n-1,n-1)
    while e not in distance[-1]:
        step = []
        for x,y in distance[-1]:
            if x<n-1 and safe[y][x+1]:
                step.append((x+1,y))
                safe[y][x+1] = False
            if x>0 and safe[y][x-1]:
                step.append((x-1,y))
                safe[y][x-1] = False
            if y<n-1 and safe[y+1][x]:
                step.append((x,y+1))
                safe[y+1][x] = False
            if y>0 and safe[y-1][x]:
                step.append((x,y-1))
                safe[y-1][x] = False

        distance.append(step)
        # print('\n'.join(''.join('O' if (x,y) in step else ('.' if s else '#') for x,s in enumerate(line)) for y,line in enumerate(safe)))
        # input()

    answer1 = len(distance) - 1

    for i in range(fallen,len(incoming)):
        unsafe = set(incoming[:i])
        print(i,incoming[i-1])
        # print('\n'.join(''.join('#' if (x,y) in unsafe else '.' for x in range(n)) for y in range(n)))

        covered = {(0,0)}
        last = [(0,0)]
        while last and e not in covered:
            step = []
            for x,y in last:
                if x<n-1 and (x+1,y) not in unsafe and (x+1,y) not in covered:
                    step.append((x+1,y))
                    covered.add((x+1,y))
                if x>0 and (x-1,y) not in unsafe and (x-1,y) not in covered:
                    step.append((x-1,y))
                    covered.add((x-1,y))
                if y<n-1 and (x,y+1) not in unsafe and (x,y+1) not in covered:
                    step.append((x,y+1))
                    covered.add((x,y+1))
                if y>0 and (x,y-1) not in unsafe and (x,y-1) not in covered:
                    step.append((x,y-1))
                    covered.add((x,y-1))
            last = step
        if e in covered:
            # print(i,'found path',incoming[i-1])
            pass
        else:
            answer2 = ','.join(str(j) for j in incoming[i-1])
            break

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
