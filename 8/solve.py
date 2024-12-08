
import collections

def solve(puzzle):
    answer1 = 0
    answer2 = 0
    lines = puzzle.splitlines()
    antennas = collections.defaultdict(set)
    antinodes = set()
    antinodes2 = set()
    h = len(lines)
    w = len(lines[0])
    for i in range(h):
        for j in range(w):
            if lines[i][j].isalnum():
                antennas[lines[i][j]].add((i,j))
    # print(antennas)
    for freq,coords in antennas.items():
        for y1,x1 in coords:
            for y2,x2 in coords:
                if (y1,x1) == (y2,x2):
                    continue
                antinodes.add( (y1+y1-y2, x1+x1-x2) )
                antinodes.add( (y2+y2-y1, x2+x2-x1) )

                for i in range(h+w):
                    antinodes2.add( (y1+(y1-y2)*i, x1+(x1-x2)*i) )
                    antinodes2.add( (y2+(y2-y1)*i, x2+(x2-x1)*i) )

    # print(antinodes)
    # print({(y,x) for y,x in antinodes if y in range(h) and x in range(w)})
    # for i in range(h):
        # print(''.join('#' if (i,j) in antinodes else '.' for j in range(w)))
    answer1 = sum(1 for y,x in antinodes if y in range(h) and x in range(w))
    answer2 = sum(1 for y,x in antinodes2 if y in range(h) and x in range(w))


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
