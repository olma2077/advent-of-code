import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def run_deer(deer, duration):
    full_cycles = deer["runtime"] * deer["speed"] * (duration // deer["cycle"])
    incomplete_cycle = deer["speed"] * min(deer["runtime"], duration % deer["cycle"])

    return full_cycles + incomplete_cycle


def solver(filename):
    deers = {}

    with open(filename) as file:
        for line in file:
            deer, speed, runtime, rest = re.fullmatch(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line.strip()).groups()
            deers[deer] = {
                "runtime": int(runtime),
                "speed": int(speed),
                "cycle": int(runtime) + int(rest)
            }

    return max([
        run_deer(deer, 2503) for deer in deers.values()
    ])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
