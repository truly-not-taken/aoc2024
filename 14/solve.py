
import re

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    w = 101
    h = 103

    p = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
    data = []
    for m in p.finditer(puzzle):
        px,py,vx,vy = map(int,m.groups())
        # print(px,py,vx,vy)
        data.append((px,py,vx,vy))

    if all(px<11 and py<7 for px,py,vx,vy in data):
        # to make test work
        w = 11
        h = 7

    grid = [[0]*w for i in range(h)]
    for px,py,vx,vy in data:
        n = 100
        x = (px+vx*n) % w
        y = (py+vy*n) % h
        grid[y][x] += 1

    # for line in grid:
        # print(''.join(map(str,line)))

    q1 = sum(grid[y][x] for y in range(h//2) for x in range(w//2))
    q2 = sum(grid[y][x] for y in range(h//2+1,h) for x in range(w//2))
    q3 = sum(grid[y][x] for y in range(h//2) for x in range(w//2+1,w))
    q4 = sum(grid[y][x] for y in range(h//2+1,h) for x in range(w//2+1,w))
    # print(q1,q2,q3,q4)

    answer1 = q1*q2*q3*q4

    n = 0

    vertical = 0 if h>100 else 1
    horizontal = 0 if w>100 else 1
    # choice = ''
    while not (vertical and horizontal):
        lines = [sum(line) for line in grid]
        columns = [sum(column) for column in zip(*grid)]
        # print(lines.count(0),min(lines),max(lines),columns.count(0),min(columns),max(columns))

        # choice=input('Is it a tree? ([y]es/[v]ertical mess/[h]orizontal mess/[N]o)') if n else ''
        # if choice.startswith('y'):
            # break
        # if choice.startswith('v'):
            # vertical = n
        # if choice.startswith('h'):
            # horizontal = n

        count_empty = 5
        lineup = 20
        # detect when robots kind of line up horizontaly
        if lines.count(0)>count_empty and max(lines)>lineup:
            horizontal = n

        # detect when robots kind of line up verticaly
        if columns.count(0)>count_empty and max(columns)>lineup:
            vertical = n

        n += 1

        if vertical and horizontal:
            # print(vertical,horizontal)
            for i in range(n,n+h*w):
                if (i-vertical)%w ==0 and (i-horizontal)%h == 0:
                    n = i
                    break

        grid = [[0]*w for i in range(h)]
        for px,py,vx,vy in data:
            x = (px+vx*n) % w
            y = (py+vy*n) % h
            grid[y][x] += 1

        # print(n)

    for line in grid:
        print(''.join(map(lambda i: str(i) if i>0 else '.',line)))

    answer2 = n

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
