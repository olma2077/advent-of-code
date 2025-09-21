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


def perimeters(regions):
    perimeters = []

    for region in regions:
        perimeter = 0

        for x, y in region:
            perimeter += 4
            neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            perimeter -= sum(1 for dx, dy in neighbours if (x + dx, y + dy) in region)

        perimeters.append(perimeter)

    return perimeters


def areas(regions):
    return [len(region) for region in regions]


def solver(filename):
    garden = []
    with open(filename) as file:
        garden = [line.strip() for line in file]

    regions = detect_regions(garden)

    return sum(p * s for p, s in zip(perimeters(regions), areas(regions)))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
