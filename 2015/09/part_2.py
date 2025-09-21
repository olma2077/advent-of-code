import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def longest_distance(graph, start, path):
    # backtracking approach with selecting a maximum possible path distance
    path.append(start)
    longest_dst = 0

    # if not all locations visited
    if len(path) < len(graph):
        longest_dst = float("-inf")

        for next_loc, dst in graph[start]:
            if next_loc not in path:
                longest_dst = max(
                    longest_dst,
                    dst + longest_distance(graph, next_loc, path)
                )

    path.pop()
    return longest_dst


def solver(filename):
    graph = {}

    with open(filename) as file:
        for edge in file:
            src, dst, weight = re.fullmatch(r"(\w+) to (\w+) = (\d+)", edge.strip()).groups()
            graph[src] = graph.get(src, []) + [(dst, int(weight))]
            graph[dst] = graph.get(dst, []) + [(src, int(weight))]

    return max([longest_distance(graph, start, []) for start in graph])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
