import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    # here goes a solution
    # with open(filename) as file:
    #     line = file.readline()
    # or
    #     for line in file:
    ...


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
