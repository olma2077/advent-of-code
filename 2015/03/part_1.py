import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    # manage visited houses as set of coordinates
    houses = set()
    x, y = 0, 0
    houses.add((x, y))

    with open(filename) as file:
        for line in file:
            for i, c in enumerate(line):
                match c:
                    case '^':
                        y += 1
                    case '>':
                        x += 1
                    case '<':
                        x -= 1
                    case 'v':
                        y -= 1

                houses.add((x, y))

    return len(houses)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
