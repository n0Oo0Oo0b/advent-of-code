import re
import numpy as np


def parse(i):
    result = re.findall(r'(turn on|turn off|toggle) (.{1,3}),(.{1,3}) through (.{1,3}),(.{1,3})', i)[0]
    cmd = result[0]
    params = [int(i) for i in result[1:]]
    params[2] += 1
    params[3] += 1
    return cmd, *params


with open('day6.txt') as file:
    data = [parse(i) for i in file.read().split('\n')]


grid = np.zeros((1000, 1000), int)
for cmd in data:
    match cmd:
        case 'turn on', x1, y1, x2, y2:
            grid[x1:x2, y1:y2] += 1
        case 'turn off', x1, y1, x2, y2:
            for x in range(x1, x2):
                for y in range(y1, y2):
                    if grid[x, y] > 0:
                        grid[x, y] -= 1
        case 'toggle', x1, y1, x2, y2:
            grid[x1:x2, y1:y2] += 2

print(sum(sum(grid)))
