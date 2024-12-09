import itertools

def solve(puzzle):
    answer1 = 0
    answer2 = 0

    disk = puzzle.strip()
    file_id = 0
    blocks = []
    for file, free in itertools.zip_longest(disk[::2],disk[1::2]):
        blocks.extend([file_id]*int(file))
        file_id += 1
        if free is None:
            break
        blocks.extend([None]*int(free))
    # print(blocks)
    blocks2 = blocks.copy()
    i = 0
    j = len(blocks)-1
    while True:
        while i<j and blocks[i] is not None:
            i+=1
        while i<j and blocks[j] is None:
            j-=1
        if i>=j:
            break
        blocks[i],blocks[j] = blocks[j],blocks[i]
    # print(blocks)

    for i, file_id in enumerate(blocks):
        if file_id is None:
            break
        answer1 += i * file_id

    # print(''.join('.' if b is None else str(b) for b in blocks2))

    j = len(blocks2)-1
    files = [int(l) for l in disk[::2]]
    while j>0:
        while 0<j and blocks2[j] is None:
            j-=1
        file_id = blocks2[j]
        l = files[file_id]
        i = blocks2.index(None)
        while i<j and any(blocks2[i:i+l]):
            i+=1
        if i<j and not any(blocks2[i:i+l]):
            print(i,j)
            blocks2[i:i+l] = [file_id]*l
            blocks2[j-l+1:j+1] = [None]*l

            # print(''.join('.' if b is None else str(b) for b in blocks2))

        while 0<j and blocks2[j]==file_id:
            j-=1

    for i, file_id in enumerate(blocks2):
        if file_id is None:
            continue
        answer2 += i * file_id

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
