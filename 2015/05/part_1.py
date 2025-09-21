import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def is_nice(string):
    vowels = 0
    double = False
    pairs = False

    # check letter pairs in loop
    for i in range(len(string) - 1):
        if string[i] in 'aeuio':
            vowels += 1
        # vowels are checked in single, so check the last char separately
        if i == len(string) - 2 and string[i + 1] in 'aeuio':
            vowels += 1

        if string[i] == string[i + 1]:
            double = True

        if string[i:i + 2] in ('ab', 'cd', 'pq', 'xy'):
            pairs = True

    return all((vowels >= 3, double, not pairs))


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
