import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def is_levels_safe(levels):
        # normalize set to asc order to unify
        if levels[0] > levels[-1]:
            levels = levels[::-1]

        for i in range(1, len(levels)):
            delta = levels[i] - levels[i - 1]
            if delta < 1 or delta > 3:
                return False

        return True


    reports = []

    with open(filename) as file:
        for line in file:
            reports.append([int(s) for s in line.split()])

    return sum(1 for report in reports if is_levels_safe(report))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
