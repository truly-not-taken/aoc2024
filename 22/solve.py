
import tqdm

def find_seq(seq,ch):
    # print(seq, ch[:20])
    for i in range(len(ch)-len(seq)):
        if ch[i:i+len(seq)]==seq:
            return i+len(seq)


def solve(puzzle):
    answer1 = 0
    answer2 = 0

    prices = []
    changes = []
    for line in tqdm.tqdm(puzzle.splitlines()):
        n = int(line)
        # print(n)

        ones = [n%10]
        for i in range(2000):
            n ^= (n << 6)
            n %= 16777216
            n ^= (n >> 5)
            n %= 16777216
            n ^= (n * 2048)
            n %= 16777216
            ones.append(n%10)

        answer1 += n

        prices.append(ones)
        changes.append([b-a for a,b in zip(ones,ones[1:])])

        # i = find_seq([-2,1,-1,3], changes[-1])
        # if i:
            # answer2 += ones[i]
    seqss = []
    for j in tqdm.tqdm(range(len(prices))):
        seqs = {}
        # 1 initial value 2000 generated values 4 wide slice
        for i in range(1+2000-4):
            ch = tuple(changes[j][i:i+4])
            if ch not in seqs:
                seqs[ch] = prices[j][i+4]
        seqss.append(seqs)

    allseqs = set()
    for seqs in tqdm.tqdm(seqss):
        allseqs.update(seqs.keys())

    answer2 = max(sum(seqs.get(k,0) for seqs in seqss) for k in tqdm.tqdm(allseqs))

    # for k in tqdm.tqdm(allseqs):
        # if sum(seqs.get(k,0) for seqs in seqss) == answer2:
            # print(k)
            # break

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
