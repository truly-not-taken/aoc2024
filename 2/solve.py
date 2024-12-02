
def safe(diffs):
    return (all(d>0 for d in diffs) or all(d<0 for d in diffs)) and all(abs(d)<=3 for d in diffs)

def part1(puzzle):
    answer = 0
    for line in puzzle.splitlines():
        numbers = [int(i) for i in line.split()]
        answer += safe([a-b for a,b in zip(numbers,numbers[1:])])
    return answer

def part2(puzzle):
    answer = 0
    for line in puzzle.splitlines():
        numbers = [int(i) for i in line.split()]
        dampened = [numbers.copy() for i in range(len(numbers))]
        for i in range(len(numbers)):
            del dampened[i][i]
        dampened.append(numbers)
        answer += any(safe([a-b for a,b in zip(n,n[1:])]) for n in dampened)
    return answer


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
