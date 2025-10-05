import os
import re
import time

INPUT = [
    'input.txt'
]


def solver(filename):
    # zero Sue is a target Sue
    target_Sue = {
        "children": "3",
        "cats": "7",
        "samoyeds": "2",
        "pomeranians": "3",
        "akitas": "0",
        "vizslas": "0",
        "goldfish": "5",
        "trees": "3",
        "cars": "2",
        "perfumes": "1",
    }

    Sues = []
    with open(filename) as file:
        for line in file:
            t1, v1, t2, v2, t3, v3 = re.fullmatch(
                r"Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",
                line.strip()).groups()

            Sues += [{
                t1: v1,
                t2: v2,
                t3: v3
            }]

    for i, Sue in enumerate(Sues):
        if all([Sue[trait] == target_Sue[trait] for trait in Sue]):
            return i + 1


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
