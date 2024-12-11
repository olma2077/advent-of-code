import os
import time
from functools import cache

INPUT = [
    'input.tst',
    'input.txt'
]


@cache
def blink(x, n):
    '''DP with cache FTW!'''
    if n == 0:
        return 1

    match x:
        case 0:
            return blink(1, n - 1)
        case _ if not len(str(x)) % 2:
            i = str(x)
            return blink(int(i[:len(i) // 2]), n - 1) + blink(int(i[len(i) // 2:]), n - 1)
        case _:
            return blink(x * 2024, n - 1)


def solver(filename):
    stones = []
    with open(filename) as file:
        stones = [int(x) for x in file.readline().split()]

    return sum(blink(stone, 75) for stone in stones)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
