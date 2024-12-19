import os
import time

INPUT = [
    'input.tst',
    'input.txt'
]

def show_wh(wh):
    '''outputs the whole warehouse, used for debug only'''
    box = False
    for x in range(10):
        for y in range(20):
            if [x, y] in wh['walls']:
                print('#', end='')
            elif [x, y] in wh['boxes']:
                if box:
                    print(']', end='')
                    box = False
                else:
                    print('[', end='')
                    box = True
            elif [x, y] == wh['robot']:
                print('@', end='')
            else:
                print('.', end='')
        print()
    input()


def solver(filename):
    def can_move(obj, diff):
        pos = [obj[0] + diff[0], obj[1] + diff[1]]
        return pos not in wh['walls'] and pos not in wh['boxes']

    def move(objs, diff):
        # same as before, but for list of objects
        if all(can_move(obj, diff) for obj in objs):
            for obj in objs:
                obj[0] += diff[0]
                obj[1] += diff[1]
            return True

        # any of boxes hit a wall
        if any([obj[0] + diff[0], obj[1] + diff[1]] in wh['walls'] for obj in objs):
            return False

        if any([obj[0] + diff[0], obj[1] + diff[1]] in wh['boxes'] for obj in objs):
            # collect all boxes we're hitting in
            boxes = []
            for obj in objs:
                pos = [obj[0] + diff[0], obj[1] + diff[1]]

                if pos in wh['boxes'] and pos not in boxes:
                    box_idx = wh['boxes'].index(pos)
                    boxes.append(wh['boxes'][box_idx])
                    # only if moving up or down we handle 2 parts of the box
                    if diff[0]:
                        if box_idx % 2:
                            if wh['boxes'][box_idx - 1] not in boxes:
                                boxes.append(wh['boxes'][box_idx - 1])
                        else:
                            if wh['boxes'][box_idx + 1] not in boxes:
                                boxes.append(wh['boxes'][box_idx + 1])

            if move(boxes, diff):
                for obj in objs:
                    obj[0] += diff[0]
                    obj[1] += diff[1]
                return True

            return False

    wh = {
        'robot': [],
        'walls': [],
        'boxes': []
    }
    moves = ''

    with open(filename) as file:
        x = 0
        while (line := file.readline().strip()) != '':
            # read map until empty line
            for y, c in enumerate(line):
                match c:
                    case '#':
                        wh['walls'].append([x, 2 * y])
                        wh['walls'].append([x, 2 * y + 1])
                    case '@':
                        wh['robot'] = [x, 2 * y]
                    case 'O':
                        wh['boxes'].append([x, 2 * y])
                        wh['boxes'].append([x, 2 * y + 1])
            x += 1

        for line in file:
            moves += line.strip()

    # show_wh(wh)
    for m in moves:
        match m:
            case '>':
                direction = (0, 1)
            case 'v':
                direction = (1, 0)
            case '<':
                direction = (0, -1)
            case '^':
                direction = (-1, 0)

        move([wh['robot']], direction)
        # show_wh(wh)

    # show_wh(wh)

    return sum(box[0] * 100 + box[1] for i, box in enumerate(wh['boxes']) if not i % 2)


for filename in INPUT:
    if os.path.exists(filename):
        start = time.perf_counter()
        answer = solver(filename)
        stop = time.perf_counter()

        print(f'Answer for {filename} got in {stop - start:0.6f}s: \n {answer}')
