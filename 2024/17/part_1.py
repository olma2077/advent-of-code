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
    def combo(x):
        return x if x < 4 else register[x - 4]

    register = [0, 0, 0]
    program = []
    with open(filename) as file:
        i = 0
        while line := file.readline().strip():
            match = re.match(r'Register (A|B|C): (\d+)', line)
            register[i] = int(match.group(2))
            i += 1

        program = [int(x) for x in file.readline().split(' ')[1].split(',')]

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

    return ','.join([str(x) for x in out])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
