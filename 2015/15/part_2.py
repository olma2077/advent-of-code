import os
import re
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def gen_recepies(ingridients, left, recepie=None):
    # classic recursive combination with dict quirks
    if not recepie:
        # recepie starting state, each ingridient should be preset 1 spoon min
        recepie = {ingridient: 1 for ingridient in ingridients}
    else:
        # copy dict as it will be updated
        recepie = recepie.copy()

    # lazy way to prune invalid combinations
    if sum(recepie.values()) > 100:
        return []

    # if only 1 ingridient left to add, just fill up to 100 spoons
    if len(left) == 1:
        recepie[left[0]] = 100 - sum(recepie.values()) + 1
        return [recepie]

    recepies = []
    # try all possible combinations of ingridients amounts
    for i in range(1, 100):
        recepie[left[0]] = i
        recepies += gen_recepies(ingridients, left[1:], recepie)

    return recepies


def eval_recepie(ingridients, recepie):
    score = 1
    calories = 0

    # iterate over each property and calc partial score for ingridients quantity in a recepie
    for property in ["capacity", "durability", "flavor", "texture"]:
        score *= max(0, sum([
            ingridients[ingridient][property] * quantity for ingridient, quantity in recepie.items()
        ]))

    # adding calories calculation in recepie evaluation
    calories = sum([
        ingridients[ingridient]["calories"] * quantity for ingridient, quantity in recepie.items()
    ])

    return score, calories


def eval_optimal_mix(ingridients):
    recepies = gen_recepies(ingridients, list(ingridients))

    return max([
        # same selecting max value but filtering by calories value
        eval_recepie(ingridients, recepie)[0] for recepie in recepies if eval_recepie(ingridients, recepie)[1] == 500
    ])


def solver(filename):
    ingridients = {}

    with open(filename) as file:
        for line in file:
            ingridient, capacity, durability, flavor, texture, calories = \
                re.fullmatch(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line.strip()).groups()

            ingridients[ingridient] = {
                "capacity": int(capacity),
                "durability": int(durability),
                "flavor": int(flavor),
                "texture": int(texture),
                "calories": int(calories),
            }

        return eval_optimal_mix(ingridients)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
