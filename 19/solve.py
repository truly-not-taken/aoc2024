
import functools

def possible(design, towels):
    if design in towels:
        return True
    return any(possible(design[len(t):],towels) for t in towels if design[:len(t)] == t)

@functools.cache
def arrangements(design, towels):
    if len(design)==0:
        return 1
    r = sum(arrangements(design[len(t):],towels) for t in towels if design[:len(t)] == t)
    return r

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    lines = puzzle.splitlines()
    towels = tuple(lines[0].split(', '))
    desired = lines[2:]

    answer1 = sum(possible(design, towels) for design in desired)


    answer2 = sum(arrangements(design, towels) for design in desired)

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
