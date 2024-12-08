import os
import time
from collections import defaultdict

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def compute_antinodes(freq):
        '''Determine all antinodes for a given frequency'''
        antinodes = set()

        # process all frequency pairs
        for i, freq_a in enumerate(freq[:-1]):
            for j, freq_b in enumerate(freq[i + 1:]):
                # distance between antennas, assume b is left and a is right
                dx, dy = freq_a[0] - freq_b[0], freq_a[1] - freq_b[1]

                nodes = []
                # left antinode is on the left from the left antenna
                nodes.append((freq_b[0] - dx, freq_b[1] - dy))
                # right antinode is on the right from the right antenna
                nodes.append((freq_a[0] + dx, freq_a[1] + dy))

                #verify if antinode is within the area:
                for x, y in nodes:
                    if x >= 0 and y >= 0 and x < m and y < n:
                        antinodes.add((x, y))

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
