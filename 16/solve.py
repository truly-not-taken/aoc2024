
import time

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    grid = [list(line) for line in puzzle.splitlines()]

    n = len(grid[0])

    x = 1
    y = n-2
    # print(x,y,grid[y][x])
    # print(*(''.join(line) for line in grid),sep='\n')
    d = '>'

    path = [[(x,y,d,0,set())]]
    min_score = 2**62
    min_score = 165544
    min_scores = [[min_score for i in range(n)] for j in range(n)]
    min_scores[y][x] = 0
    t = time.time()
    best = set()
    while path:
        if not path[-1]:
            path.pop()
            if path:
                p = path[-1].pop()
                # if (1,10) in p[4]:
                    # print('<===',p)
                    # print(*(''.join('@' if ((i,j)==(p[0],p[1])) else ch for i,ch in enumerate(line)) for j,line in enumerate(grid)),sep='\n')
            continue

        x,y,d,score,visited = path[-1][-1]
        # if x==1 and y == 10:
            # print('???',x,y,d)
            # for p in path:
                # print(p)

        if score>min_scores[y][x]+1001 or grid[y][x] == '#' or (x,y) in visited:
            # if len(path)==4:
                # print('wall',x,y,d)
                # for p in path:
                    # print(p)
            path[-1].pop()
            continue
        min_scores[y][x] = score
        if grid[y][x] == 'E' and score <= min_score:
            print('SCORE!')
            print(x,y,d,score, len(path), min_score)
            path[-1].pop()
            if score < min_score:
                min_score = score
                best = visited | {(x,y)}
            else:
                best.update(visited)
            print(*(''.join('O' if (i,j) in best else ch for i,ch in enumerate(line)) for j,line in enumerate(grid)),sep='\n')
            continue

        tt = time.time()
        if tt-t>1:
            t=tt
            print(*(''.join(str((s*9//min_score)%10) if s<1_000_000 else '.' for s in line) for line in min_scores),sep='\n')
            print()
        # print(*(''.join('@' if ((i,j)==(x,y)) else ch for i,ch in enumerate(line)) for j,line in enumerate(grid)),sep='\n')
        # print(x,y,d,score, len(path), min_score)
        # for p in path:
            # print(p)

        v = visited | {(x,y)}
        if d=='>':
            path.append([(x+1,y,'>',score+1, v), (x,y-1,'^',score+1001, v), (x,y+1,'v',score+1001, v)])
        elif d=='<':
            path.append([(x-1,y,'<',score+1, v), (x,y-1,'^',score+1001, v), (x,y+1,'v',score+1001, v)])
        elif d=='v':
            path.append([(x,y+1,'v',score+1, v), (x-1,y,'<',score+1001, v), (x+1,y,'>',score+1001, v)])
        elif d=='^':
            path.append([(x,y-1,'^',score+1, v), (x-1,y,'<',score+1001, v), (x+1,y,'>',score+1001, v)])
        else:
            return 'error'

        # print('add',path[-1])
        # print()

    answer1 = min_score
    answer2 = len(best)

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
