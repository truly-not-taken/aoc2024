
def blink(x):

    r = []

    for i in x:
        if i==0:
            r.append(1)
            continue
        s = str(i)
        if len(s) % 2 == 0:
            r.append(int(s[:len(s)//2]))
            r.append(int(s[len(s)//2:]))
            continue
        r.append(i*2024)
    return r

cache = {}

def blink2(stone, times):
    cached = cache.get((stone, times))
    # print(stone, times, cached)
    if cached is not None:
        return cached

    if times == 0:
        return 1

    if stone == 0:
        r = blink2(1,times-1)
        cache[(stone, times)] = r
        return r
    s = str(stone)
    if len(s) % 2 == 0:
        r = blink2(int(s[:len(s)//2]), times-1) + blink2(int(s[len(s)//2:]), times-1)
        cache[(stone, times)] = r
        return r

    r = blink2(stone*2024, times-1)
    cache[(stone, times)] = r
    return r

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    numbers = [int(i) for i in puzzle.strip().split()]
    print(numbers)

    # answer1 = numbers
    # for i in range(25):
        # answer1 = blink(answer1)
        # print(i, answer1)
    # answer1 = len(answer1)

    answer1 = sum(blink2(i,25) for i in numbers)
    answer2 = sum(blink2(i,75) for i in numbers)

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
