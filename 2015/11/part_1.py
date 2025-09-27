import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def next_passwd(passwd):
    passwd = [ord(c) - ord('a') for c in passwd]

    while True:
        # incrementing base 26 number with carry over
        i = -1
        passwd[i] += 1

        while passwd[i] // 26:
            # if a digit is overflown, carry over and move to the next
            passwd[i] %= 26
            i -= 1
            passwd[i] += 1

        yield ''.join([chr(x + ord('a')) for x in passwd])


def is_valid(passwd):
    # no i, o, l
    for c in passwd:
        if c in "iol":
            return False

    n = len(passwd)

    # at least one triplet of consequent letters
    triplet = False
    for i in range(n - 2):
        if ord(passwd[i]) + 2 == ord(passwd[i + 1]) + 1 == ord(passwd[i + 2]):
            triplet = True
            break
    if not triplet:
        return False

    # two distinct different pairs of letters
    pair = 0
    for i in range(1, n):
        if passwd[i] == passwd[i - 1]:
            if not pair:
                # first pair found
                pair = i
            elif pair + 1 < i and passwd[i] != passwd[pair]:
                # second pair is not overlapping and differs from first
                return True


def solver(filename):
    with open(filename) as file:
        for line in file:
            passwds = next_passwd(line.strip())
            for passwd in passwds:
                if is_valid(passwd):
                    return passwd


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
