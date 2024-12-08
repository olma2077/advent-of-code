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
            for i, c in enumerate(line.strip()):
                if c == '(':
                    floor += 1
                else:
                    floor -= 1
                if floor < 0:
                    return i + 1

    return i + 1


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
