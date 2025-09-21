import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def turn_off(x1, y1, x2, y2, lights):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[y][x] = False


def turn_on(x1, y1, x2, y2, lights):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[y][x] = True


def toggle(x1, y1, x2, y2, lights):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[y][x] = not lights[y][x]


def solver(filename):
    lights = [[False] * 1000 for _ in range(1000)]

    with open(filename) as file:
        for instruction in file:
            match re.fullmatch(
                r"(turn off|toggle|turn on) (\d+),(\d+) through (\d+),(\d+)",
                instruction.strip()).groups():
                case ("turn off", x1, y1, x2, y2):
                    turn_off(*[int(i) for i in (x1, y1, x2, y2)], lights)
                case ("toggle", x1, y1, x2, y2):
                    toggle(*[int(i) for i in (x1, y1, x2, y2)], lights)
                case ("turn on", x1, y1, x2, y2):
                    turn_on(*[int(i) for i in (x1, y1, x2, y2)], lights)
                case other:
                    print(f'Parsing error: {other}')

    return sum(sum(1 for light in row if light) for row in lights)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
