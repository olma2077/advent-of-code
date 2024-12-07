import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    warehouse = []
    guard = None

    with open(filename) as file:
        for line in file:
            # find guard starting position while reading the file
            if not guard:
                col = line.find('^')
                if col >= 0:
                    guard = [len(warehouse), col]

            warehouse.append(list(line.strip()))

    m = len(warehouse)
    n = len(warehouse[0])

    # possible guard moving directions as deltas to use a loop for movement
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    x, y = guard
    steps = 0
    direction = 0
    # guard moves until exits warehouse
    while x < m and x >= 0 and y < n and y >= 0:
        if warehouse[x][y] == '#':
            # step back if we walked into an obstacle
            x -= directions[direction][0]
            y -= directions[direction][1]

            # cycle through direction deltas
            direction = (direction + 1) % 4

        elif warehouse[x][y] != 'X':
            # mark cell if we haven't visit it yet
            steps += 1
            warehouse[x][y] = 'X'

        # move guard
        x += directions[direction][0]
        y += directions[direction][1]

    return steps


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
