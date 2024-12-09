import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def expand_diskmap(diskmap):
    blocks = []

    for i, block_size in enumerate(diskmap):
        # alternate between empty space and a file block
        block = '.' if i % 2 else i // 2
        blocks += [block] * int(block_size)

    return blocks


def defragment_blocks(blocks):
    j = len(blocks) - 1

    # optimization 1: store file ID of the last file we tried to move.
    # As IDs are initially monotonically ascending, we can ignore
    # anything not smaller then the previously processed file.
    file_id = None

    # optimization 2: store the smallest file size we failed to move.
    # As files are moved from end to start of the disk, there won't
    # be more empty space, we can skip files with size not less than
    # we couldn't move earlier.
    unmovable_filesize = float('inf')

    while j >= 0:
        # find a file from end of the disk
        # optimization 1: skip already moved files
        while blocks[j] == '.' or file_id and blocks[j] >= file_id:
            j -= 1

        # optimization 1: remember the file id we're to move
        file_id = blocks[j]

        # find the file size
        k = 0
        while blocks[j - k] == blocks[j]:
            k += 1

        # optimization 2: skip file if size is too big
        if k >= unmovable_filesize:
            j -= k
            continue

        # find empty block of a suitable size from start of the disk
        i = 0
        while True:
            # skip to a beginning of an empty space
            while i < j and blocks[i] != '.':
                i += 1

            # if empty space is behind the file, nowhere to move it
            if i >= j:
                # optimization 2: remember size of the file which we couldn't move
                unmovable_filesize = min(k, unmovable_filesize)
                break

            # if empy space size fits move the file and proceed with a next file
            if ['.'] * k == blocks[i:i + k]:
                blocks[i:i + k], blocks[j - k + 1:j + 1] = \
                blocks[j - k + 1:j + 1], blocks[i:i + k]
                break

            # skip space otherwise
            while blocks[i] == '.':
                i += 1

        # skip to the end of the file
        j -= k

    return blocks


def checksum(blocks):
    return sum(i * block for i, block in enumerate(blocks) if block != '.')


def solver(filename):
    diskmap = ''
    with open(filename) as file:
        diskmap = file.readline()

    blocks = expand_diskmap(diskmap)
    blocks = defragment_blocks(blocks)

    return checksum(blocks)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
