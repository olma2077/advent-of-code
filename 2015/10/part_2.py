import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def look_and_say(number):
    prev, count = number[0], 0
    new_number = ''

    for i, c in enumerate(number):
        if c == prev:
            count += 1
        else:
             new_number += str(count) + prev
             prev = c
             count = 1

    new_number += str(count) + prev

    return new_number

def solver(filename):
    number = ''

    with open(filename) as file:
        number = file.readline()

    for _ in range(50):
        number = look_and_say(number)

    return len(number)

for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
