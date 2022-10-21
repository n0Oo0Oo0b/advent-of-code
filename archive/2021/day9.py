import numpy as np
from itertools import product

with open('day9.txt') as file:
    data = np.array([[int(j) for j in list(i)] for i in file.read().split('\n')], int)


sizeX = len(data)
sizeY = len(data[0])


def adjacentLocs(point):
    x, y = point
    adjacent = []
    if x > 0:
        adjacent.append((x - 1, y))
    if x < sizeX - 1:
        adjacent.append((x + 1, y))
    if y > 0:
        adjacent.append((x, y - 1))
    if y < sizeY - 1:
        adjacent.append((x, y + 1))
    return adjacent


t = 0
lowPoints = set()
highPoints = set()
for x, y in product(range(sizeX), range(sizeY)):
    loc = data[x, y]
    if loc != 9:
        adjacent = [data[x] for x in adjacentLocs((x, y))]
        if min(adjacent) > loc:
            t += loc + 1
            lowPoints.add((x, y))
    else:
        highPoints.add((x, y))


basinSizes = []

for i, lowPoint in enumerate(lowPoints):
    basinPoints = {lowPoint}

    # Runs code until the floodfill is complete
    lastSize = 0
    while lastSize != len(basinPoints):
        lastSize = len(basinPoints)
        
        # Find all adjacent points that are not 9
        adjacent = set()
        for point in basinPoints:
            adjacent = adjacent.union(adjacentLocs(point))
        
        # Add new points onto the basin
        basinPoints = basinPoints.union(adjacent.difference(highPoints))
    
    # Store the basin
    basinSizes.append(len(basinPoints))

# Output
largest = sorted(basinSizes, reverse=True)[:3]
print(f'Part 1: {t}\nPart 2: {largest[0]*largest[1]*largest[2]}')
