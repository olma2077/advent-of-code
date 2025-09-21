import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def enc_count(string):
    # add outer "" symbols for a string
    count = 2

    i = 0
    while i < len(string):
        # escape \ and "
        if string[i] in ("\\", "\""):
            count += 1

        count += 1
        i += 1

    return count


def solver(filename):
    literal_len, enc_len = 0, 0

    with open(filename) as file:
        for string in file:
            literal_len += len(string.strip())
            enc_len += enc_count(string.strip())

    return enc_len - literal_len


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
