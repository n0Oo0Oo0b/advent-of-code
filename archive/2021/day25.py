with open('inputs/day25.txt') as file:
    data = file.read().splitlines()
outputData = ''


GENERATE_OUTPUT = True
SIZE_Y = len(data)
SIZE_X = len(data[0])

# Create a set of east-facing and south-facing sea cucumber by location
east, south = set(), set()
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == 'v':
            south.add((j, i))
        elif char == '>':
            east.add((j, i))


allCucumbers = east.union(south)  # Set of location of all sea cucumber
steps = 0  # Number of steps
change = True  # Flag of whether a cucumber has moved on the step
while change and (steps := steps + 1):
    change = False
    
    for i, cucumbers in enumerate((east, south)):  # east move before south
        # Keep a copy of the group before their movement is calculated
        prevState = cucumbers.copy()
        cucumbers.clear()
        for x, y in prevState:
            # Calculates position in front of sea cucumber
            f = (x, (y + 1) % SIZE_Y) if i else ((x + 1) % SIZE_X, y)
            
            if f in allCucumbers:
                cucumbers.add((x, y))  # Spot is blocked, 'move' to the same spot
            else:
                cucumbers.add(f)  # Spot is free, move cucumber
                change = True
        
        # Update allCucumbers to match the newly moved sea cucumber
        allCucumbers.difference_update(prevState)
        allCucumbers.update(cucumbers)
        
    if GENERATE_OUTPUT:
        for y in range(SIZE_Y):
            for x in range(SIZE_X):
                if (x, y) in allCucumbers:
                    outputData += '>' if (x, y) in east else 'v'
                else:
                    outputData += ' '
            outputData += '\n'
        outputData += '\n\n\n'

print(steps)

if GENERATE_OUTPUT:
    with open('day25_output.txt', 'w') as outputFile:
        outputFile.write(outputData)
