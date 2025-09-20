import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def repr_count(string):
    count = 0

    i = 1
    while i < len(string) - 1:
        if string[i:i + 2] == "\\x":
            count += 1
            i += 4
        elif string[i] == "\\":
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count


def solver(filename):
    literal_len, repr_len = 0, 0

    with open(filename) as file:
        for string in file:
            literal_len += len(string.strip())
            repr_len += repr_count(string.strip())

    return literal_len - repr_len


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
