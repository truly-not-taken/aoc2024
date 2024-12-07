

def solve(puzzle):
    answer1 = 0
    answer2 = 0
    m = [['E',*l,'E'] for l in puzzle.splitlines()]
    e = ['E']*len(m[0])
    m = [e, *m, e]
    for j,line in enumerate(m):
        for i,spot in enumerate(line):
            if spot=='^':
                x,y = i,j
                break
    start = x,y
    newmap = tuple(tuple(line) for line in m)

    dx,dy = 0,-1
    while m[y][x] != 'E':
        m[y][x] = 'X'
        if m[y+dy][x+dx] != '#':
            x+=dx
            y+=dy
        else:
            dx,dy = {
                (0,-1):(1,0),
                (1,0):(0,1),
                (0,1):(-1,0),
                (-1,0):(0,-1),
            }[(dx,dy)]

    answer1 = sum(spot=='X' for line in m for spot in line)

    oldpath = m
    for oy in range(len(m)):
        for ox in range(len(m[0])):

            # print(oy,ox,'   ',end='\r',flush=True)
            m = list(list(line) for line in newmap)
            if oldpath[oy][ox] != 'X':
                continue
            m[oy][ox] = '#'

            x,y = start
            direction = '^'
            dx,dy = 0,-1
            m[y][x] = '.'

            while m[y][x] != 'E':
                if direction in m[y][x]:
                    # print('\n'.join(''.join((spot if type(spot)==str else '+') for spot in l) for l in m))
                    answer2 += 1
                    break
                if type(m[y][x]) == str:
                    m[y][x] = [direction]
                else:
                    m[y][x].append(direction)
                if m[y+dy][x+dx] != '#':
                    x+=dx
                    y+=dy
                else:
                    direction, dx,dy = {
                        (0,-1):('>',1,0),
                        (1,0):('v',0,1),
                        (0,1):('<',-1,0),
                        (-1,0):('^',0,-1),
                    }[(dx,dy)]
    # print()
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
