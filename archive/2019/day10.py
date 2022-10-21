import numpy as np
from itertools import product, cycle
from collections import defaultdict


def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


def get_angles(current, others):
    directions = defaultdict(list)
    
    phases = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    
    x, y = current
    for asteroid in others:
        if current == asteroid:
            continue
        
        x_2, y_2 = asteroid
        dx, dy = x_2 - x, y - y_2
        
        phase = phases.index((sign(dx), sign(dy)))
        v = (abs(dx)+abs(dy), asteroid)
        if phase % 2 == 0:
            directions[(phase, )].append(v)
        else:
            gradient = dx/dy if phase in (1, 5) else -dy/dx
            directions[(phase, gradient)].append(v)
    
    for lst in directions.values():
        lst.sort()
        
    return directions


with open('day10.txt') as file:
    data = list(map(str.strip, file))

size = len(data)
grid = np.zeros((size, size), bool)
asteroids = set()
for y, row in enumerate(data):
    for x, item in enumerate(row):
        if item == '#':
            asteroids.add((x, y))
            grid[x, y] = True
        else:
            grid[x, y] = False


max_location, max_count = None, 0
for x, y in asteroids:
    directions = get_angles((x, y), asteroids)
    count = len(directions)
    if count > max_count:
        max_count = count
        max_location = (x, y)

print(max_count)

asteroids.remove(max_location)
angles = get_angles(max_location, asteroids)
all_angles = sorted(angles)

destroy_count = 0
last_destroyed = None
for direction in cycle(all_angles):
    if angles[direction]:
        last_destroyed = angles[direction].pop(0)[1]
        destroy_count += 1
        if destroy_count == 200:
            break

print(f'{last_destroyed[0]}{last_destroyed[1]:02}')
