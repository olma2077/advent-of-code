import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    '''DP approach'''
    def is_x(x, y):
        '''check if there's valid X-MAS with center in (x, y) cell'''
        # define all possible positions for M, S as deltas from A to check in loop
        delta = [((-1, -1), (1, 1)),
                ((1, 1), (-1, -1)),
                ((-1, 1), (1, -1)),
                ((1, -1), (-1, 1))]

        # we need two MAS to form an X
        count = 0
        for M, S in delta:
            if matrix[x + M[0]][y + M[1]] == 'M':
                # we have MA
                if matrix[x + S[0]][y + S[1]] != 'S':
                    # but not MAS
                    return False
                else:
                    count += 1

        return True if count == 2 else False

    matrix = []

    with open(filename) as file:
        for line in file:
            matrix.append(line.strip())

    n = len(matrix[0])
    m = len(matrix)

    count = 0
    # walk possible centers of X and check if there's a valid X-MAS
    # NB border cells can't be center of an X, so skipping them
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if matrix[i][j] == 'A':
                count += 1 * is_x(i, j)

    return count


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
