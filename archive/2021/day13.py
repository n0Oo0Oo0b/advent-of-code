import numpy as np
import re
from random import randint


with open('day13.txt') as file:
    a, b = tuple(file.read().split('\n\n'))
    locs = {(int((x := i.split(','))[0]), int(x[1])) for i in a.split('\n')}
    folds = [((x := re.findall(r'([xy])=(\d+)', i)[0])[0], int(x[1])) for i in b.split('\n')]


for i in range(len(folds)):
    axis, loc = folds[i]
    new = set()
    for x, y in locs:
        if (x if (a := axis == 'x') else y) > loc:
            if a:
                x = loc * 2 - x
            else:
                y = loc * 2 - y
        new.add((x, y))
    locs = new
    if i == 0:
        l = len(locs)


grid = np.zeros((max(map(lambda x: x[1], locs))+1, max(map(lambda x: x[0], locs))+1), int)
for x, y in locs:
    grid[y, x] = 1

p2 = '\n'.join([''.join(map(str, line)).replace('1', '██').replace('0', '  ') for line in grid])

print(f'Part 1: {l}\nPart 2 (CAPTCHA):\n{p2}')
