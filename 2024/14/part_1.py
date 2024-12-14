import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]

# some changable constants
N = 101
M = 103
T = 100


def move_robot(robot, steps):
    robot['x'] = (robot['x'] + robot['vx'] * steps) % N
    robot['y'] = (robot['y'] + robot['vy'] * steps) % M


def solver(filename):
    robots = []
    with open(filename) as file:
        for line in file:
            match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
            robot = {
                'x': int(match.group(1)),
                'y': int(match.group(2)),
                'vx': int(match.group(3)),
                'vy': int(match.group(4))
            }
            robots.append(robot)

    for robot in robots:
        move_robot(robot, T)

    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if robot['x'] < N // 2 and robot['y'] < M // 2:
            q1 += 1
        if robot['x'] < N // 2 and robot['y'] > M // 2:
            q2 += 1
        if robot['x'] > N // 2 and robot['y'] < M // 2:
            q3 += 1
        if robot['x'] > N // 2 and robot['y'] > M // 2:
            q4 += 1

    return q1 * q2 * q3 * q4


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
