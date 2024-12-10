import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def is_nice(string):
    double_pair = False
    separated_pair = False

    for i in range(len(string) - 2):
        # double pair
        if string[i:i + 2] in string[i + 2:]:
            double_pair = True

        # separated pair
        if string[i] == string[i + 2]:
            separated_pair = True

    return all((double_pair, separated_pair))


def solver(filename):
    strings = []
    with open(filename) as file:
        strings = [line.strip() for line in file]

    return sum(1 for string in strings if is_nice(string))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
