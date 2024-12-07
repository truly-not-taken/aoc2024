
def solve(puzzle):
    answer1 = 0
    answer2 = 0
    for line in puzzle.splitlines():
        left, right = line.split(':')
        test_value = int(left)
        words = right.strip().split()
        numbers = [int(i) for i in words]

        results = [numbers[0]]
        ops = [0]
        while ops[0]<2:
            if ops[-1] == 0:
                results.append(results[-1] + numbers[len(results)])
            elif ops[-1] == 1:
                results.append(results[-1] * numbers[len(results)])
            else:
                results.pop()
                ops.pop()
                ops[-1] = ops[-1] + 1
                continue

            if len(results) < len(numbers) and results[-1] <= test_value:
                ops.append(0)
            else:
                if results[-1] == test_value:
                    answer1 += test_value
                    break
                ops[-1] = ops[-1] + 1
                results.pop()

        results = [numbers[0]]
        ops = [0]
        while ops[0]<3:
            if ops[-1] == 0:
                results.append(results[-1] + numbers[len(results)])
            elif ops[-1] == 1:
                results.append(results[-1] * numbers[len(results)])
            elif ops[-1] == 2:
                results.append(int(str(results[-1]) + words[len(results)]))
            else:
                results.pop()
                ops.pop()
                ops[-1] = ops[-1] + 1
                continue

            if len(results) < len(numbers) and results[-1] <= test_value:
                ops.append(0)
            else:
                if results[-1] == test_value:
                    answer2 += test_value
                    break
                ops[-1] = ops[-1] + 1
                results.pop()

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
