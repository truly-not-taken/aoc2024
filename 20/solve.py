
import tqdm

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    grid = tuple(puzzle.splitlines())
    n = len(grid[0])

    picoseconds = 100 if n==141 else 2
    picoseconds2 = 100 if n==141 else 50


    # print(*grid,sep='\n')
    # print()

    path = [(i,j) for i,line in enumerate(grid) for j,ch in enumerate(line) if ch =='S']
    y,x = path[0]
    while grid[y][x] != 'E':
        next_step = [(y+dy,x+dx) for dy,dx in ((0,1), (0,-1), (1,0), (-1,0)) if grid[y+dy][x+dx] in '.E']
        # print(next_step)
        if len(next_step)>1:
            next_step.remove(path[-2])
        y,x = next_step[0]
        path.append((y,x))

    # print(len(path)-1)

    # pathset = set(path[1:-1])
    # for y in range(n):
        # print(''.join('O' if (y,x) in pathset else grid[y][x] for x in range(n)))
    # print()

    cheats = []
    for i,(y1,x1) in enumerate(tqdm.tqdm(path)):
        for j,(y2,x2) in enumerate(path[i+2+picoseconds::2]):
            if abs(y1-y2) + abs(x1-x2)==2:
                # print(j*2+2, i,j,(y1,x1),(y2,x2))
                # cheats += 1
                cheats.append(((y1+y2)//2,(x1+x2)//2))
    # for y in range(n):
        # print(''.join('C' if (y,x) in cheats else grid[y][x] for x in range(n)))

    cheats2 = 0
    for i,(y1,x1) in enumerate(tqdm.tqdm(path)):
        for j,(y2,x2) in enumerate(path[i+picoseconds2:]):
            cheat_len = abs(y1-y2) + abs(x1-x2)
            save = j + picoseconds2 - cheat_len
            if cheat_len <= 20 and save >= picoseconds2:
                # print(save, cheat_len, i,j,(y1,x1),(y2,x2))
                cheats2 += 1
                # for y in range(n):
                    # print(''.join('C' if y in range(min(y1,y2),max(y1,y2)+1) and x in range(min(x1,x2),max(x1,x2)+1) else grid[y][x] for x in range(n)))
                # input()

    answer1 = len(cheats)
    # not 5691

    answer2 = cheats2

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
