import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def get_trail_score(x, y, summits, level = 0):
        # out of map
        if x < 0 or y < 0 or x == n or y == m:
            return 0

        # trail is not uphill
        if topo[x][y] != level:
            return 0

        # trail is complete, remember reached summit
        if topo[x][y] == 9:
            summits.add((x, y))
            return 0

        # directions to move in loop
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # ignore unique summits count form a middle of a trail
        [get_trail_score(x + dx, y + dy, summits, level + 1) for dx, dy in delta]

        # count unique summits from trailhead
        return len(summits)

    topo = []

    with open(filename) as file:
        for line in file:
            topo.append([int(c) for c in line.strip()])

    n = len(topo)
    m = len(topo[0])

    return sum(get_trail_score(x, y, set()) for x in range(n) for y in range(m))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
