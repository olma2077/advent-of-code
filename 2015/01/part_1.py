import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    floor = 0

    with open(filename) as file:
        for line in file:
            floor += sum(1 if c == '(' else -1 for c in line)

    return floor



for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
