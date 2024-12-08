import os
import time
from collections import defaultdict

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def compute_antinodes(antennas):
        '''Determine all antinodes for a given frequency'''
        antinodes = set()

        # process all frequency pairs
        for i, ant_a in enumerate(antennas[:-1]):
            for j, ant_b in enumerate(antennas[i + 1:]):
                # distance between antennas, assume b is left and a is right
                dx, dy = ant_a[0] - ant_b[0], ant_a[1] - ant_b[1]

                # calculate deltas to compute antinodes in loop
                delta = ((dx, dy), (-dx, -dy))

                for dx, dy in delta:
                    # start from one of antennas
                    x, y = ant_a

                    while x >= 0 and y >= 0 and x < m and y < n:
                        # as antennas are also antinodes we add
                        # all resonance nodes within area
                        antinodes.add((x, y))
                        x += dx
                        y += dy

        return antinodes

    # store antennas' coordinates in a dict, grouped by frequency
    antennas = defaultdict(list)

    with open(filename) as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                if c != '.':
                    antennas[c].append((i, j))

    # area size
    m = i + 1
    n = j + 1

    antinodes = set()
    for freq in antennas:
        antinodes |= compute_antinodes(antennas[freq])

    return len(antinodes)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
