import itertools

def solve(puzzle):
    answer1 = 0
    answer2 = 0
    for line in puzzle.splitlines():
        left, right = line.split(':')
        left = int(left)
        numbers = [int(i) for i in right.strip().split()]
        print(left, numbers)
        for binary in range(2**len(numbers)-1):
            ops = ['+' if binary&(1<<j) else '*' for j in range(len(numbers)-1)]
            n = iter(numbers)
            r = next(n)
            for op, i in zip(ops,n):
                if op == '+':
                    r += i
                else:
                    r *= i
            # print(ops, r)
            if r==left:
                # print(left, numbers, ops)
                answer1 += left
                break

        for ternary in range(3**len(numbers)-1):
            ops = [['+','*','||'][ternary // 3**j % 3] for j in range(len(numbers)-1)]
            n = iter(numbers)
            r = next(n)
            for op, i in zip(ops,n):
                if op == '+':
                    r += i
                elif op == '*':
                    r *= i
                else:
                    r = int(str(r)+str(i))
            # print(ops, r)
            if r==left:
                print(left, numbers, ops)
                answer2 += left
                break

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
