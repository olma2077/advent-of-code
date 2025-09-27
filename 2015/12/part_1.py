import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    string = ''
    with open(filename) as file:
        string = file.readline()

    # no need to parse json, just regexp match numbers
    numbers = re.findall(r'(-?\d+)', string)

    return sum([int(n) for n in numbers])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
