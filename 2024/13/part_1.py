import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


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
                'P': [int(x) for x in P.groups()]
            }
            machines.append(machine)

            if not file.readline():
                break

    total_tokens = 0
    for machine in machines:
        a_press = 0

        while a_press * machine['A'][0] < machine['P'][0]:
            # dumb bruteforce
            if not (machine['P'][0] - a_press * machine['A'][0]) % machine['B'][0]:
                # if we can press A and B in such combination to get to X of prise
                b_press = (machine['P'][0] - a_press * machine['A'][0]) // machine['B'][0]

                if a_press * machine['A'][1] + b_press * machine['B'][1] == machine['P'][1]:
                    # check if we hit Y of prise as well
                    total_tokens += 3 * a_press + b_press
                    break

            a_press += 1

    return total_tokens


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
