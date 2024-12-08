
import collections

def solve(puzzle):
    answer1 = 0
    answer2 = 0
    lines = puzzle.splitlines()
    antennas = collections.defaultdict(list)
    antinodes = set()
    antinodes2 = set()
    n = len(lines)
    for i in range(n):
        for j in range(n):
            if lines[i][j].isalnum():
                antennas[lines[i][j]].append((i,j))
    for freq,coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i+1,len(coords)):
                y1,x1 = coords[i]
                y2,x2 = coords[j]

                y3,x3 = (y1+y1-y2, x1+x1-x2)
                if y3 in range(n) and x3 in range(n):
                    antinodes.add( (y3,x3) )
                y3,x3 = (y2+y2-y1, x2+x2-x1)
                if y3 in range(n) and x3 in range(n):
                    antinodes.add( (y3,x3) )

                for multiple in range(n):
                    y3,x3 = (y1+(y1-y2)*multiple, x1+(x1-x2)*multiple)
                    if y3 not in range(n) or x3 not in range(n):
                        break
                    antinodes2.add( (y3,x3) )
                for multiple in range(n):
                    y3,x3 = (y2+(y2-y1)*multiple, x2+(x2-x1)*multiple)
                    if y3 not in range(n) or x3 not in range(n):
                        break
                    antinodes2.add( (y3,x3) )

    answer1 = len(antinodes)
    answer2 = len(antinodes2)

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
