
def gps(warehouse):
    return sum(y*100 + x for y,line in enumerate(warehouse) for x,ch in enumerate(line) if ch == 'O' or ch == '[')

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    data = puzzle.splitlines()
    split = data.index('')
    warehouse = [list(line) for line in data[:split]]
    instructions = ''.join(data[split+1:])

    # print(*warehouse,sep='\n')
    # print(len(instructions))

    robot = [(x,y) for y,line in enumerate(warehouse) for x,ch in enumerate(line) if ch=='@']
    if len(robot)==1:
        x,y = robot[0]
    else:
        return 'error robot'

    wide = [list(line.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')) for line in data[:split]]
    # print(*(''.join(line) for line in wide),sep='\n')

    robot = [(x,y) for y,line in enumerate(wide) for x,ch in enumerate(line) if ch=='@']
    if len(robot)==1:
        wx,wy = robot[0]
    else:
        return 'error wide robot'


    for i in instructions:
        # print(i)
        if i=='<':
            dx=-1
            dy=0
        elif i=='^':
            dx=0
            dy=-1
        elif i=='>':
            dx=1
            dy=0
        elif i=='v':
            dx=0
            dy=1
        else:
            return 'error instruction'

        xx = x + dx
        yy = y + dy
        while warehouse[yy][xx]=='O':
            xx += dx
            yy += dy
        if warehouse[yy][xx]=='.':
            warehouse[yy][xx] = 'O'
            warehouse[y][x] = '.'
            x += dx
            y += dy
            warehouse[y][x] = '@'

        # print(*(''.join(line) for line in warehouse),sep='\n')

        if dy==0:
            xx = wx + dx
            while wide[wy][xx] in '[]':
                xx += dx
            if wide[wy][xx]=='.':
                while xx!=wx:
                    wide[wy][xx] = wide[wy][xx-dx]
                    xx -= dx
                wide[wy][wx] = '.'
                wx += dx
                wide[wy][wx] = '@'
        else:
            move = [[ch == '@' for ch in line] for line in wide]
            y_range = range(len(move))
            if dy == -1:
                y_range = reversed(y_range)
            wall = False
            for yy in y_range:
                for xx, m in enumerate(move[yy]):
                    if not m:
                        continue
                    # print(xx,yy)
                    if wide[yy+dy][xx] == ']':
                        move[yy+dy][xx] = True
                        move[yy+dy][xx-1] = True
                    elif wide[yy+dy][xx] == '[':
                        move[yy+dy][xx] = True
                        move[yy+dy][xx+1] = True
                    elif wide[yy+dy][xx] == '#':
                        wall = True
                        break
            if not wall:
                y_range = range(len(move))
                if dy == 1:
                    y_range = reversed(y_range)
                for yy in y_range:
                    for xx, m in enumerate(move[yy]):
                        if m:
                            wide[yy+dy][xx] = wide[yy][xx]
                            wide[yy][xx] = '.'
                wy += dy


        # print(*(''.join(line) for line in wide),sep='\n')
        # input()
    # print(*(''.join(line) for line in wide),sep='\n')

    answer1 = gps(warehouse)
    answer2 = gps(wide)

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
