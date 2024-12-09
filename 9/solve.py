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
    first_free = 0
    files = [int(l) for l in disk[::2]]
    file_id = len(files)
    not_fit = 10
    while j>first_free:
        file_id -= 1
        l = files[file_id]
        if l >= not_fit:
            continue
        while blocks2[j] != file_id:
            j-=1
        i = first_free = blocks2.index(None, first_free)

        len_free = 0
        while len_free != l and i<j:
            if blocks2[i] is None:
                len_free += 1
            else:
                len_free = 0
            i += 1
        i -= len_free

        if len_free == l:
            # print(i,j)
            blocks2[i:i+l] = [file_id]*l
            blocks2[j-l+1:j+1] = [None]*l
            # print(''.join('.' if b is None else str(b) for b in blocks2))
        else:
            not_fit = l

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
