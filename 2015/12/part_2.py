import json
import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def evaluate(item):
    if isinstance(item, list):
        # for list sum of elements
        return sum([evaluate(el) for el in item])
    elif isinstance(item, int):
        # for int return value
        return item
    elif isinstance(item, dict):
        # for dict first check if any property is 'red'
        if 'red' in item.values():
            return 0
        else:
            return sum([evaluate(el) for el in item.values()])
    elif isinstance(item, str):
        # ignore strings
        return 0
    else:
        # never should get here
        print(item)
        raise


def solver(filename):
    string = ''
    with open(filename) as file:
        string = file.readline()

    ledger = json.loads(string)
    for item in ledger:
        total += evaluate(item)

    return sum([evaluate(item) for item in ledger])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
