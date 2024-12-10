import itertools

def score(topomap, x, y, step):
    n = len(topomap)
    if x not in range(n) or y not in range(n):
        return set()
    if topomap[y][x]!=step:
        return set()
    if step==9:
        return {(x,y),}
    return (
        score(topomap, x+1, y, step+1) |
        score(topomap, x-1, y, step+1) |
        score(topomap, x, y+1, step+1) |
        score(topomap, x, y-1, step+1)
    )

def score2(topomap, x, y, step):
    n = len(topomap)
    if x not in range(n) or y not in range(n):
        return 0;
    if topomap[y][x]!=step:
        return 0
    if step==9:
        return 1
    return (
        score2(topomap, x+1, y, step+1) +
        score2(topomap, x-1, y, step+1) +
        score2(topomap, x, y+1, step+1) +
        score2(topomap, x, y-1, step+1)
    )


def solve(puzzle):
    answer1 = 0
    answer2 = 0

    topomap = [[int(c) for c in line] for line in puzzle.strip().splitlines()]
    n = len(topomap)
    # print(topomap, n)
    for y in range(n):
        for x in range(n):
            s = score(topomap, x, y, 0)

            answer1 += len(s)

            s = score2(topomap, x, y, 0)
            answer2 += s

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
