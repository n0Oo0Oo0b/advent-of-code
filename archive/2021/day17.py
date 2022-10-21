import re
from itertools import product

with open('inputs/day17.txt') as file:
    xMin, xMax, yMin, yMax = (int(i) for i in re.findall(r'.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', file.read())[0])

accepted = 0

for xV, yV in product(range(xMax + 10), range(yMin - 5, 700)):
    x = 0
    y = 0
    while y >= yMin and x <= xMax:
        if xMin <= x and y <= yMax:
            accepted += 1
            break
        
        x += xV
        y += yV
        
        if xV > 0:
            xV -= 1
        yV -= 1

print(yMin * (yMin + 1) // 2, accepted)
