
def find_region(grid,x,y):
    n = len(grid[0])
    plant = grid[y][x]
    answer = set()
    deep = [(x,y)]
    while deep:
        next_deep = []
        for xx,yy in deep:
            if xx not in range(n) or yy not in range(n):
                continue
            if (xx,yy) not in answer and grid[yy][xx] == plant:
                answer.add((xx,yy))
                next_deep.append((xx+1,yy))
                next_deep.append((xx-1,yy))
                next_deep.append((xx,yy+1))
                next_deep.append((xx,yy-1))
        deep = next_deep
    # print(plant, answer)
    return answer

def perimeter(region):
    # print('perimeter', region)
    p = 0
    for x,y in region:
        p += (x+1,y) not in region
        p += (x-1,y) not in region
        p += (x,y+1) not in region
        p += (x,y-1) not in region
    return p

def sides(region):
    # print('sides', region)
    n = set()
    s = set()
    w = set()
    e = set()
    for x,y in region:
        if (x+1,y) not in region:
            e.add((x+1,y))
        if (x-1,y) not in region:
            w.add((x-1,y))
        if (x,y+1) not in region:
            s.add((x,y+1))
        if (x,y-1) not in region:
            n.add((x,y-1))

    answer = 0
    while e:
        answer += 1
        x,y = e.pop()

        yy = y - 1
        while (x,yy) in e:
            e.remove((x,yy))
            yy -= 1
        yy = y + 1
        while (x,yy) in e:
            e.remove((x,yy))
            yy += 1

    while w:
        answer += 1
        x,y = w.pop()

        yy = y - 1
        while (x,yy) in w:
            w.remove((x,yy))
            yy -= 1
        yy = y + 1
        while (x,yy) in w:
            w.remove((x,yy))
            yy += 1

    while s:
        answer += 1
        x,y = s.pop()

        xx = x - 1
        while (xx,y) in s:
            s.remove((xx,y))
            xx -= 1
        xx = x + 1
        while (xx,y) in s:
            s.remove((xx,y))
            xx += 1

    while n:
        answer += 1
        x,y = n.pop()

        xx = x - 1
        while (xx,y) in n:
            n.remove((xx,y))
            xx -= 1
        xx = x + 1
        while (xx,y) in n:
            n.remove((xx,y))
            xx += 1

    return answer

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    grid = puzzle.split()

    n = len(grid[0])
    # print(n)

    regions = []
    for y in range(n):
        for x in range(n):
            if all((x,y) not in r for r in regions):
                regions.append(find_region(grid,x,y))
    # print(regions)

    answer1 = sum(len(r) * perimeter(r) for r in regions)
    answer2 = sum(len(r) * sides(r) for r in regions)

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
