import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    '''DP approach'''
    word = 'XMAS'

    def find_all(x, y, letter_idx, direction = None):
        '''Find all XMAS words starting from (x, y) cell'''
        # word completed
        if letter_idx == len(word):
            return True

        # out of bounds
        if x < 0 or y < 0 or x == m or y == n:
            return False

        # wrong letter
        if matrix[x][y] != word[letter_idx]:
            return False

        if not direction:
            # first letter, we can choose any direction
            # define all possible directions as deltas to walk in loop
            delta = [(0, 1), (1, 0), (0, -1), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
            return sum(find_all(x + dx, y + dy, letter_idx + 1, (dx, dy)) for dx, dy in delta)
        else:
            # follow selected direction
            dx, dy = direction
            return find_all(x + dx, y + dy, letter_idx + 1, direction)

    matrix = []

    with open(filename) as file:
        for line in file:
            matrix.append(line.strip())

    n = len(matrix[0])
    m = len(matrix)

    return sum(find_all(x, y, 0) for x in range(m) for y in range(n))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
