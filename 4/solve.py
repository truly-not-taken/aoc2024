
import re

def count_xmas(puzzle):
    a = sum(line.count('XMAS')+line.count('SAMX') for line in puzzle)
    return a

def part1(puzzle):
    answer = 0
    horizontal = puzzle.splitlines()
    # for line in puzzle.splitlines():
    answer += count_xmas(horizontal)
    vertical = [''.join(i) for i in zip(*horizontal)]
    answer += count_xmas(vertical)
    diagonal1 = [''.join(i) for i in zip(*[' '*j+''.join(data)+' '*(len(data)-1-j) for j,data in enumerate(horizontal)])]
    answer += count_xmas(diagonal1)
    diagonal2 = [''.join(i) for i in zip(*[' '*(len(data)-1-j)+''.join(data)+' '*j for j,data in enumerate(horizontal)])]
    answer += count_xmas(diagonal2)

    return answer

def part2(puzzle):
    answer = 0
    data = puzzle.splitlines()
    l = len(data[0])
    for i in range(1,l-1):
        for j in range(1,l-1):
            if data[i][j]=='A' and {data[i-1][j-1],data[i+1][j+1]}=={'M','S'} and {data[i-1][j+1],data[i+1][j-1]}=={'M','S'}:
                answer+=1

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
