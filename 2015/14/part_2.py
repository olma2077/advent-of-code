import os
import re
import time

from collections import defaultdict

INPUT = [
    'input.tst',
    'input.txt'
]


def run_deer(deer):
    # deer runnung iterator, returns distance covered by a deer each second
    duration = 0

    while True:
        duration += 1
        full_cycles = deer["runtime"] * deer["speed"] * (duration // deer["cycle"])
        incomplete_cycle = deer["speed"] * min(deer["runtime"], duration % deer["cycle"])

        yield full_cycles + incomplete_cycle


def solver(filename):
    deers = {}

    with open(filename) as file:
        for line in file:
            deer, speed, runtime, rest = re.fullmatch(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line.strip()).groups()
            deers[deer] = {
                "runtime": int(runtime),
                "speed": int(speed),
                "cycle": int(runtime) + int(rest),
                "points": 0,
            }

    # initialize deers running iterators
    for name, deer in deers.items():
        deer["running"] = run_deer(deers[name])

    for _ in range(2503):
        # for each second get a distance and a list of deers who run it
        distances = defaultdict(list)
        for name, deer in deers.items():
            distance = deer["running"].__next__()
            distances[distance] += [name]

        for name in distances[max(distances)]:
            # add point for all deers with max distance this second
            deers[name]["points"] += 1

    return max([
        deer["points"] for deer in deers.values()
    ])

for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
