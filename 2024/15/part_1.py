import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]


def solver(filename):
    wh = {
        'robot': [],
        'walls': [],
        'boxes': []
    }
    moves = ''

    with open(filename) as file:
        def move(obj, pos):
            if pos not in wh['walls'] and pos not in wh['boxes']:
                # update coordinates by value for inplace change
                # to avoid removing/adding boxes/robot coordinates
                obj[0], obj[1] = pos[0], pos[1]
                return True

            if pos in wh['boxes']:
                # try to recursively move the box and any boxes in front of it
                box_idx = wh['boxes'].index(pos)
                box = wh['boxes'][box_idx]
                new_pos = [
                    pos[0] + (pos[0] - obj[0]),
                    pos[1] + (pos[1] - obj[1])
                ]
                if move(box, new_pos):
                    obj[0], obj[1] = pos[0], pos[1]
                    return True

            # either hit a wall or couldn't move a box
            return False

        x = 0
        while (line := file.readline().strip()) != '':
            # read map until empty line
            for y, c in enumerate(line):
                match c:
                    case '#':
                        wh['walls'].append([x, y])
                    case '@':
                        wh['robot'] = [x, y]
                    case 'O':
                        wh['boxes'].append([x, y])
            x += 1

        for line in file:
            moves += line.strip()

    for m in moves:
        match m:
            case '>':
                position = [wh['robot'][0], wh['robot'][1] + 1]
            case 'v':
                position = [wh['robot'][0] + 1, wh['robot'][1]]
            case '<':
                position = [wh['robot'][0], wh['robot'][1] - 1]
            case '^':
                position = [wh['robot'][0] - 1, wh['robot'][1]]

        move(wh['robot'], position)

    return sum(x * 100 + y for x, y in wh['boxes'])


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
