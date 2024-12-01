
import collections

def part1(puzzle):
    left = []
    right = []
    for line in puzzle.splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    return sum(abs(l-r) for l, r in zip(left, right))

def part2(puzzle):
    left = []
    right = collections.Counter()
    for line in puzzle.splitlines():
        l, r = line.split()
        left.append(int(l))
        right[int(r)] += 1
    return sum(l * right[l] for l in left)


def main():
    filename = 'input.txt'
    import sys
    if len(sys.argv)>1:
        filename = sys.argv[1]
    with open(filename) as file:
        puzzle = file.read()
        print('part1:', part1(puzzle))
        print('part2:', part2(puzzle))

if __name__ == '__main__':
    main()
