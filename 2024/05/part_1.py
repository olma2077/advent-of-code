import os
import time
from collections import defaultdict

INPUT = [
    'input.tst',
    'input.txt'
]

def solver(filename):
    def is_valid(seq):
        '''DP approach to check if print sequence is valid'''
        # single (last) page is always a valid sequence
        if len(seq) == 1: return True

        # NB rules are exhaustive: if B can be after B, there is a rule for it
        # there are no implicit rules like if A|B and B|C then A|C
        # there should be explicit rules for all "before, after" pages

        return all([next in order[seq[0]] for next in seq[1:]] + [is_valid(seq[1:])])
        #           ^if next page can     ^for all "next"         ^should be valid for
        #            follow first page     pages after first       each page in seq

    order = defaultdict(list)
    prints = []

    with open(filename) as file:
        rules = True

        for line in file:
            line = line.strip()
            if line == '':
                # we've scanned all rules
                rules = False

            elif rules == True:
                # scan order rules in a following dict:
                # key: preceding page
                # value: list of allowed following pages
                x, y = [int(a) for a in line.split('|')]
                order[x].append(y)

            elif rules == False:
                # scan print sequences
                prints.append([int(a) for a in line.split(',')])

    count = 0
    for seq in prints:
        if not is_valid(seq):
            count += seq[len(seq) // 2]

    return count

for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
