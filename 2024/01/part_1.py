import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    a = []
    b = []

    with open(filename) as file:
        for line in file:
            x, y = line.split()
            a.append(int(x))
            b.append(int(y))

    a.sort()
    b.sort()

    return sum([abs(x - y) for x, y in zip(a, b)])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
