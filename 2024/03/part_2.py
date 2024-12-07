import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    count = 0

    with open(filename) as file:
        do = True

        for line in file:
            for match in re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', line):
                match match.groups():
                    case _ if match.group() == "do()":
                        do = True
                    case _ if match.group() == "don't()":
                        do = False
                    case (x, y):
                        x, y = int(x), int(y)
                        count += x * y * do

    return count


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
