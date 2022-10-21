import numpy as np  # yes, I use numpy


def parse(line):  # Parses a line of the puzzle input
    start, end = tuple(line.split(' -> '))
    return [int(i) for i in start.split(',')], [int(i) for i in end.split(',')]


#  Puzzle input
with open('day5.txt') as file:
    data = [parse(i) for i in file.read().split('\n')]


def customRange(start, end):  # similar to built-in range() but inclusive and step is ±1
    if start < end:
        return range(start, end+1)
    else:
        return range(start, end-1, -1)


# grid only stores H/V lines (part 1), grid2 stores diagonal lines as well (part 2)
grid = np.zeros((1000, 1000), int)
grid2 = np.zeros((1000, 1000), int)

for point1, point2 in data:
    if point1[0] == point2[0]:  # Horizontal lines
        for i in customRange(point1[1], point2[1]):
            grid[point1[0], i] += 1
            grid2[point1[0], i] += 1
    elif point1[1] == point2[1]:  # Vertical lines
        for i in customRange(point1[0], point2[0]):
            grid[i, point1[1]] += 1
            grid2[point1[0], i] += 1
    else:  # Diagonal lines
        for x, y in zip(customRange(point1[0], point2[0]), customRange(point1[1], point2[1])):
            grid2[x, y] += 1

print(f'Part 1: {(grid > 1).sum()}\nPart 2: {(grid2 > 1).sum()}')  # this is why I use numpy
