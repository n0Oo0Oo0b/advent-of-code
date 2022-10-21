import numpy as np
from itertools import product


def parse(dat):
    # [id] @ [startX],[startY]: [SIZE_X]x[SIZE_Y]
    start, size = tuple(dat.split(' @ ')[1].split(': '))
    start, size = tuple(map(int, start.split(','))), tuple(map(int, size.split('x')))
    startX, startY = start
    sizeX, sizeY = size
    endX, endY = startX + sizeX, startY + sizeY
    return startX, endX, startY, endY


with open('day3.txt') as file:
    data = [parse(i.strip()) for i in file.readlines()]

fabric = np.zeros((1000, 1000))
for startX, endX, startY, endY in data:
    fabric[startX:endX, startY:endY] += 1

overlap = fabric > 1
print(sum(sum(overlap)))

fabric = np.zeros((1000, 1000))
for startX, endX, startY, endY in data:
    o = False
    for x, y in product(range(startX, endX), range(startY, endY)):
        if overlap[x, y]:
            o = True
            break
    if not o:
        print(data.index((startX, endX, startY, endY))+1)
        break
