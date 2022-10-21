import numpy as np
from contextlib import suppress
from itertools import product


def getString(bitmap):
    r = ''
    for col in bitmap:
        r += ''.join(map(str, col)) + '/'
    return r[:-1].replace('0', '.').replace('1', '#')


def getPattern(string):
    string = string.replace('.', '0').replace('#', '1')
    a = []
    for i in string.split('/'):
        a.append(list(map(int, list(i))))
    return np.array(a)


with open('day21.txt') as file:
    rawData = [i.strip().split(' => ') for i in file.readlines()]
    ruleBook = {}
    for rule in rawData:
        ruleBook[rule[0]] = getPattern(rule[1])


def rotate(bitmap, angle):
    return np.rot90(bitmap, angle)


def flip(bitmap, flips):
    if 0 in flips:
        bitmap = np.flipud(bitmap)
    if 1 in flips:
        bitmap = np.flipud(bitmap)
    return bitmap


def permutations(bitmap):
    for rotation in range(4):
        for f in [[], [0], [1], [0, 1]]:
            yield getString(rotate(flip(bitmap, f), rotation))


def enhance(bitmap):
    for i in permutations(bitmap):
        with suppress(KeyError):
            return ruleBook[i]


grid = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
])

for _ in range(18):
    gridSize = grid.shape[0]
    if gridSize % 2 == 0:
        newSize = gridSize*3//2
        newGrid = np.zeros((newSize, newSize), int)
        divSize = 2
    else:
        newSize = gridSize*4//3
        newGrid = np.zeros((newSize, newSize), int)
        divSize = 3
    
    sections = [np.hsplit(i, gridSize / divSize) for i in np.vsplit(grid, gridSize / divSize)]
    sectionSize = divSize + 1
    for x, y in product(range(0, newSize, sectionSize), repeat=2):
        newGrid[x:x+sectionSize, y:y+sectionSize] = enhance(sections[x//sectionSize][y//sectionSize])
    grid = newGrid.copy()
    print(_)

print(grid)
print(grid.sum())
