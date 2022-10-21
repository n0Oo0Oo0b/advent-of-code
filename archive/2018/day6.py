import numpy as np
from itertools import product

with open('day6.txt') as file:
    data = [tuple(map(int, i.strip().split(','))) for i in file.readlines()]


def getDist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


areas = {i: 0 for i in data}
for loc in product(range(400), repeat=2):
    distances = sorted(data, key=lambda l: getDist(l, loc))
    if getDist(distances[0], loc) != getDist(distances[1], loc):
        if 0 in loc or 399 in loc:
            areas[distances[0]] = -1
        if areas[distances[0]] != -1:
            areas[distances[0]] += 1

print(max(areas.values()))

t = 0
for loc in product(range(400), repeat=2):
    totalDistance = sum([getDist(loc, i) for i in data])
    if totalDistance < 10000:
        t += 1
print(t)
