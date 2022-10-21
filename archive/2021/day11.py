import numpy as np  # Very op :)
from itertools import product


# File storing states at each step for visualisation using another script
outputFile = open('day11_output.txt', mode='w')

# Puzzle input
with open('day11.txt') as file:
    data = np.array([[int(j) for j in list(i)] for i in file.read().split('\n')], int)
    SIZE_X, SIZE_Y = data.shape  # Should be (10, 10)


def getAdjacent(point):
    """
    Returns set of all coordinates of adjacent(including diagonal) locations
    """
    xL, yL = point
    points = set()
    for x, y in product(range(xL - 1, xL + 2), range(yL - 1, yL + 2)):
        if (x, y) != point and 0 <= x < SIZE_X and 0 <= y < SIZE_Y:
            points.add((x, y))
    return points


totalFlashes = 0
step = 0
while step := step+1:  # forever loop with incrementing counter
    
    allFlash = np.zeros(data.shape, bool)  # 2D array of which locations flash on that step
    flashLocs = set()  # Location of all flashes on specific step
    
    # Increment every cell
    data += 1
    
    # Calculate all flashes
    while (data > 9).sum():
        # Calculate all locations ready to flash
        flashes = data > 9
        
        for x, y in product(range(SIZE_X), range(SIZE_Y)):
            if flashes[x, y]:  # Octopus needs to flash
                flashLocs.add((x, y))
                
                for loc in getAdjacent((x, y)):  # Increment neighbouring locations
                    if loc not in flashLocs:  # Don't increment locations that have flashed already
                        data[loc] += 1
                
                data[x, y] = 0  # Reset octopus to 0 energy
        
        # Update allFlash to include the new flashes
        allFlash = allFlash | flashes
    
    if step <= 100:  # Counts number of flashes for first 100 days (Part 1)
        totalFlashes += allFlash.sum()
    
    # Store the state of all octopuses for visualisation script
    outputFile.write(' '.join(''.join(str(i) for i in data[j]) for j in range(10))+'\n')
    
    if allFlash.all():  # Break out of loop when every octopus flashes (Part 2)
        break

# Output
print(f'Part 1: {totalFlashes}\nPart 2: {step}')
outputFile.close()
