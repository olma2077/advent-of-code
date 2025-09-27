import os
import re
import time

from collections import defaultdict

INPUT = [
    'input.tst',
    'input.txt'
]


def max_happiness(guests, seated, happines):
    # Classic backtracking: try all seating combinations, select the best
    if len(guests) == len(seated):
        # Account happiness for the final guest to close the circle
        return happines + guests[seated[-1]][seated[0]] + guests[seated[0]][seated[-1]]

    return max([
        max_happiness(guests,
                      seated + [guest],
                      happines + guests[guest][seated[-1]] + guests[seated[-1]][guest])
        for guest in guests if guest not in seated
    ])


def solver(filename):
    guests = defaultdict(dict)
    with open(filename) as file:
        for line in file:
            guest, sign, value, neighbour = re.fullmatch(
                r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).",
                line.strip()
                ).groups()
            value = int(value) * (1 if sign == "gain" else -1)

            # dict of dicts with happiness change for each pair of guests
            guests[guest][neighbour] = value

    # start with seating each guest first, as a pair of guests contribute to happiness
    return max([max_happiness(guests, [guest], 0) for guest in guests])

for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
