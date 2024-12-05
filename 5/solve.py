
import collections

def solve(puzzle):
    answer1 = 0
    answer2 = 0
    lines = iter(puzzle.splitlines())
    ordering = collections.defaultdict(set)
    while line:=next(lines):
        a, b = line.split('|')
        ordering[a].add(b)
    for line in lines:
        pages = line.split(',')
        if all(b in ordering[a] for a,b in zip(pages,pages[1:])):
            answer1 += int(pages[len(pages)//2])
        else:
            s = set(pages)
            for p in pages:
                if len(ordering[p] & s) == len(pages)//2:
                    answer2 += int(p)
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
