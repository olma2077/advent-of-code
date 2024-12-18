import os
import re
import time
from enum import Enum

INPUT = [
    'input.tst',
    'input.txt'
]

# opcodes
class Opcode(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


def solver(filename):
    def compile(register, program):
        def combo(x):
            return x if x < 4 else register[x - 4]

        p = 0
        out = []

        while p < len(program):
            match Opcode(program[p]):
                case Opcode.ADV:
                    register[0] //= 2 ** combo(program[p + 1])
                case Opcode.BXL:
                    register[1] ^= program[p + 1]
                case Opcode.BST:
                    register[1] = 7 & combo(program[p + 1])
                case Opcode.JNZ:
                    p = program[p + 1] - 2 if register[0] else p
                case Opcode.BXC:
                    register[1] ^= register[2]
                case Opcode.OUT:
                    out.append(7 & combo(program[p + 1]))
                case Opcode.BDV:
                    register[1] = register[0] // (2 ** combo(program[p + 1]))
                case Opcode.CDV:
                    register[2] = register[0] // (2 ** combo(program[p + 1]))
            p += 2

        return out

    register = [0, 0, 0]
    program = []
    with open(filename) as file:
        i = 0
        while line := file.readline().strip():
            match = re.match(r'Register (A|B|C): (\d+)', line)
            register[i] = int(match.group(2))
            i += 1

        program = [int(x) for x in file.readline().split(' ')[1].split(',')]

    a = 1
    for i in range(1, len(program) + 1):
        while program[-i:] != compile([a, 0, 0], program)[-i:]:
            a += 1
        # program depends only on A, it prints a value then shifts A right 3 bits
        # so we can recover A from the end finding suitable A for the last program byte,
        # shift right for 3 bits and add another program byte until we found the whole A
        a <<= 3

    # we have one redundant shift
    return a >> 3


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
