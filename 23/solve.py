
import collections

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    network = collections.defaultdict(set)

    for line in puzzle.splitlines():
        a,b = line.split('-')
        network[a].add(b)
        network[b].add(a)

    computers = list(network.keys())

    threes = set()
    for i,a in enumerate(computers):
        # print(network[a])
        for j,b in enumerate(computers[i+1:]):
            if a not in network[b]:
                continue
            # print(network[b])
            for k,c in enumerate(computers[i+j+1:]):
                # print(network[c])
                if a[0]!='t' and b[0]!='t' and c[0]!='t':
                    continue
                if a in network[c] and b in network[c]:
                    # print(a,b,c)
                    threes.add(frozenset({a,b,c}))
    # print(threes)
    answer1 = len(threes)

    largest = set()
    for a in computers:
        for b in network[a]:
            party = {a,b}
            for c in network[a] & network[b]:
                if network[c] & party == party:
                    party.add(c)
            if len(party) > len(largest):
                print(len(party), party)
                largest = party
    answer2 = ','.join(sorted(largest))

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
