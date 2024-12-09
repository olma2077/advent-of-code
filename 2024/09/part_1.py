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
    i, j = 0, len(blocks) - 1
    while True:
        # find empty block from start of the disk
        while blocks[i] != '.':
            i += 1

        # Find a file block from end of the disk
        while blocks[j] == '.':
            j -= 1

        # if pointers have crossed we moved all files to the start
        if j < i:
            break

        blocks[i], blocks[j] = blocks[j], blocks[i]

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
