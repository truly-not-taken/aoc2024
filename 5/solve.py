
import collections

def part1(puzzle):
    answer = 0
    lines = puzzle.splitlines()
    split = lines.index("")
    ordering = set(tuple(int(a) for a in line.split('|')) for line in lines[:split])
    updates = tuple(tuple(int(a) for a in line.split(',')) for line in lines[split+1:])
    for pages in updates:
        if all((pages[j],pages[i]) not in ordering for i in range(len(pages)-1) for j in range(i+1,len(pages))):
            answer += pages[len(pages)//2]


    return answer

def part2(puzzle):
    answer = 0
    lines = puzzle.splitlines()
    split = lines.index("")
    ordering = set(tuple(int(a) for a in line.split('|')) for line in lines[:split])
    updates = tuple(tuple(int(a) for a in line.split(',')) for line in lines[split+1:])
    for pages in updates:
        if any((pages[j],pages[i]) in ordering for i in range(len(pages)-1) for j in range(i+1,len(pages))):

            count = [b for a in pages for b in pages if (a,b) in ordering]

            for k,v in collections.Counter(count).items():
                if v==len(pages)//2:
                    answer += k

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
