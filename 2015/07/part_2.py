import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def eval_wire(wires, wire_id):
    if wire_id.isdigit():
        return int(wire_id)

    wire_input = wires[wire_id]

    if isinstance(wire_input, int):
        return wire_input

    match wire_input.split():
        case [value] if value.isdigit():
            wires[wire_id] = int(value)
        case [wire_A]:
            wires[wire_id] = eval_wire(wires, wire_A)
        case ['NOT', wire_A]:
            wires[wire_id] =  ~eval_wire(wires, wire_A) & 0xFFFF
        case [wire_A, 'AND', wire_B]:
            wires[wire_id] = (eval_wire(wires, wire_A) & eval_wire(wires, wire_B)) & 0xFFFF
        case [wire_A, 'OR', wire_B]:
            wires[wire_id] = (eval_wire(wires, wire_A) | eval_wire(wires, wire_B)) & 0xFFFF
        case [wire_A, 'LSHIFT', value]:
            wires[wire_id] = (eval_wire(wires, wire_A) << int(value)) & 0xFFFF
        case [wire_A, 'RSHIFT', value]:
            wires[wire_id] = (eval_wire(wires, wire_A) >> int(value)) & 0xFFFF

    return wires[wire_id]


def solver(filename):
    wires = {}

    with open(filename) as file:
        for instruction in file:
            wire_input, wire_id = instruction.split(' -> ')
            wires[wire_id.strip()] = wire_input

    value_a = eval_wire(wires, 'a')

    with open(filename) as file:
        for instruction in file:
            wire_input, wire_id = instruction.split(' -> ')
            wires[wire_id.strip()] = wire_input

    wires['b'] = value_a
    return eval_wire(wires, 'a')


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
