import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def follow_guard(loop_check=False):
        '''Follow guard's path until he gets looped or exits warehouse
        parameter used to select if path should be recorded or just check for a loop
        Funtion returns tuple (is_looped, path)'''
        # possible guard moving directions as deltas to use a loop for movement
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        # track pivot points with new directions to see if guard hits the same path
        pivots = set()
        # record guard visited coordinates for potential obstacles placement
        path = set()

        x, y = guard
        direction = 0
        # guard moves until exits warehouse (or looped)
        while x < m and x >= 0 and y < n and y >= 0:
            if warehouse[x][y] == '#':
                # step back if we walked into an obstacle
                x -= directions[direction][0]
                y -= directions[direction][1]

                # cycle through direction deltas
                direction = (direction + 1) % 4

                if loop_check:
                    # remember pivot point and new direction
                    # we need to remember direction as the guard
                    # can visit the came point from different directions
                    # and not necessarily be in a loop yet
                    pivot = ((x, y), directions[direction])
                    if pivot in pivots:
                        # return empty path just for consistent function signature
                        return True, path
                    pivots.add(pivot)

            if not loop_check:
                # remember position if it's not the initial one
                if warehouse[x][y] != '^':
                    path.add((x, y))

            # move guard
            x += directions[direction][0]
            y += directions[direction][1]

        # guard has left the warehouse, return his path
        return False, path

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

    loops = 0

    # get guard's path first to know where makes sence to place obstacles
    _, path = follow_guard()
    for x, y in path:
        warehouse[x][y] = '#'

        is_looped, _ = follow_guard(loop_check=True)
        loops += 1 * is_looped

        warehouse[x][y] = '.'

    return loops


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
