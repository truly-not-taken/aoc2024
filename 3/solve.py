
import re

def part1(puzzle):
    answer = 0
    for line in puzzle.splitlines():
        print(line)
        for a,b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            print(a,b)
            answer += int(a) * int(b)
    return answer

def part2(puzzle):
    answer = 0
    isEnabled = True
    for line in puzzle.splitlines():
        for a,b,do,dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", line):
            if do:
                isEnabled = True
                continue
            if dont:
                isEnabled = False
                continue
            if isEnabled:
                answer += int(a) * int(b)
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
