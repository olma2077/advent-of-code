import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]

ADD = 10000000000000

def solver(filename):
    machines = []
    with open(filename) as file:
        while file:
            A = re.match(r"Button A: X\+(\d+), Y\+(\d+)", file.readline())
            B = re.match(r"Button B: X\+(\d+), Y\+(\d+)", file.readline())
            P = re.match(r"Prize: X=(\d+), Y=(\d+)", file.readline())

            machine = {
                'A': [int(x) for x in A.groups()],
                'B': [int(x) for x in B.groups()],
                'P': [int(x) + ADD for x in P.groups()]
            }
            machines.append(machine)

            if not file.readline():
                break

    total_tokens = 0
    for m in machines:
        # intermediate calculations to make code readable
        a = m['A'][0] * m['P'][1] - m['A'][1] * m['P'][0]
        b = m['A'][0] * m['B'][1] - m['A'][1] * m['B'][0]

        # due to float division error first check if there is a div remainder
        if not a % b:
            b_press = a // b
            c = m['P'][0] - b_press * m['B'][0]

            if not c % m['A'][0]:
                a_press = c // m['A'][0]
                total_tokens += 3 * a_press + b_press

    return total_tokens


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
