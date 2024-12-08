import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    # manage visited houses as set of coordinates
    houses = set()
    houses.add((0, 0))

    # store both Santas coordinates in lists to alternate between them in a single loop
    x = [0, 0]
    y = [0, 0]

    with open(filename) as file:
        for line in file:
            for i, c in enumerate(line):
                match c:
                    case '^':
                        y[i % 2] += 1
                    case '>':
                        x[i % 2] += 1
                    case '<':
                        x[i % 2] -= 1
                    case 'v':
                        y[i % 2] -= 1

                houses.add((x[i % 2], y[i % 2]))

    return len(houses)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
