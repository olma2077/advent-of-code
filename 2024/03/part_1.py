import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    result = 0

    with open(filename) as file:
        for line in file:
            mul_ops = re.findall(r'mul\((\d+),(\d+)\)', line)
            result += sum(int(x) * int(y) for x, y in mul_ops)

    return result


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
