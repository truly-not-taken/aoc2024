
import re

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    p = re.compile(r'Button A:[^\d]*(\d+),[^\d]*(\d+)\nButton B:[^\d]*(\d+),[^\d]*(\d+)\nPrize:[^\d]*(\d+),[^\d]*(\d+)')

    for m in p.finditer(puzzle):
        ax,ay,bx,by,px,py = map(int,m.groups())
        # print(ax,ay,bx,by,px,py)

        # x = {(i, (px-ax*i)//bx) for i in range(101) if (px-ax*i)%bx==0}
        # y = {(i, (py-ay*i)//by) for i in range(101) if (py-ay*i)%by==0}
        # print(x,y, x&y)
        # for a,b in x&y:
            # print(a,divmod(px,a),divmod(py,a), a*ax+b*bx, a*ay+b*by)
            # print(b,divmod(px,b),divmod(py,b))
        # answer1 += min((3*a+b for a,b in x&y), default=0)


        a = (px*by-bx*py)//(by*ax-bx*ay)
        b = (py*ax-ay*px)//(by*ax-bx*ay)

        print(a,b, a*ax+b*bx==px, a*ay+b*by==py)
        if a in range(101) and b in range(101) and a*ax+b*bx==px and a*ay+b*by==py:
            answer1 += 3*a+b

        px += 10000000000000
        py += 10000000000000

        a = (px*by-bx*py)//(by*ax-bx*ay)
        b = (py*ax-ay*px)//(by*ax-bx*ay)

        print(a,b, a*ax+b*bx==px, a*ay+b*by==py)
        if a*ax+b*bx==px and a*ay+b*by==py:
            answer2 += 3*a+b

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
