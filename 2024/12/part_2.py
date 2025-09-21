import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def detect_regions(garden):
    '''DP with tracking visied pots'''
    def get_region(i, j, pot):
        if i < 0 or j < 0 or i == n or j == m:
            return []

        if visited[i][j]:
            return []

        if garden[i][j] != pot:
            return []

        visited[i][j] = True

        region = [(i, j)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            region += get_region(i + di, j + dj, pot)

        return region

    n = len(garden)
    m = len(garden[0])

    regions = []
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                regions.append(get_region(i, j, garden[i][j]))

    return regions


def sides(regions):
    '''Ugly corners counting'''
    sides = []

    for region in regions:
        side = 0

        for x, y in region:
            neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            # outer cormer: two consequent neighbours are missing
            for i in range(4):
                if (x + neighbours[i][0], y + neighbours[i][1]) not in region and \
                   (x + neighbours[(i + 1) % 4][0], y + neighbours[(i + 1) % 4][1]) not in region:
                       side += 1

            # inner corner: two consequent neighbours and diagonal neighbour is missing
                if (x + neighbours[i][0], y + neighbours[i][1]) in region and \
                   (x + neighbours[(i + 1) % 4][0], y + neighbours[(i + 1) % 4][1]) in region and \
                   (x + (neighbours[i][0] or neighbours[(i + 1) % 4][0]),
                    y + (neighbours[i][1] or neighbours[(i + 1) % 4][1])) not in region:
                       side += 1

        sides.append(side)

    return sides


def areas(regions):
    return [len(region) for region in regions]


def solver(filename):
    garden = []
    with open(filename) as file:
        garden = [line.strip() for line in file]

    regions = detect_regions(garden)

    return sum(p * s for p, s in zip(sides(regions), areas(regions)))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
