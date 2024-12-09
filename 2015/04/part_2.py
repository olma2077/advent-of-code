import os
import time
from hashlib import md5

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    with open(filename) as file:
        key = file.readline()
        i = 1
        # optimization: pre-encode part of the string
        key = key.encode('utf-8')

        while True:
            line = key + str(i).encode('utf-8')
            # optimization: compare slice is quicker than startswith()
            if md5(line).hexdigest()[:6] == '000000':
                return i

            i += 1


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
