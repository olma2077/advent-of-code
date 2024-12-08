import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    boxes = []
    with open(filename) as file:
        for line in file:
            boxes.append(sorted([int(x) for x in line.split('x')]))

    return sum(2 * x * y + 2 * y * z + 2 * x * z + x * y for x, y, z in boxes)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
