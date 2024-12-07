import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    def is_valid(result, ops):
        '''DP approach to check all possible combination of operations
        if any give correct result'''
        if len(ops) == 1:
            return ops[0] == result

        return is_valid(result, [ops[0] * ops[1]] + ops[2:]) or \
               is_valid(result, [ops[0] + ops[1]] + ops[2:])

    equations = []

    with open(filename) as file:
        for line in file:
            res, ops = line.strip().split(':')
            equations.append([int(res)] + [int(x) for x in ops.strip().split()])

    return sum(result for result, *operands in equations if is_valid(result, operands))


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
