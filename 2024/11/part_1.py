import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    stones = []
    with open(filename) as file:
        stones = [int(x) for x in file.readline().split()]

    for _ in range(25):
        tmp = []
        for stone in stones:
            match stone:
                case 0:
                    tmp.append(1)
                case _ if not len(str(stone)) % 2:
                    i = str(stone)
                    tmp.append(int(i[:len(i) // 2]))
                    tmp.append(int(i[len(i) // 2:]))
                case _:
                    tmp.append(stone * 2024)
        stones = tmp

    return len(stones)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
