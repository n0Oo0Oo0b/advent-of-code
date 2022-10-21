from collections import defaultdict

with open('inputs/day20.txt') as file:
    data, grid = file.read().split('\n\n')

spots = defaultdict(bool)
for x, row in enumerate(grid.split('\n')):
    for y, char in enumerate(row):
        if char == '#':
            spots[(x+150, y+150)] = True


def enhance(x, y):
    final = ''.join('1' if spots[(i, j)] else '0' for i in range(x-1, x+2) for j in range(y-1, y+2))
    return data[int(final, 2)] == '#'


for i in range(1, 51):
    new = defaultdict(bool)
    for x in range(450):
        for y in range(450):
            new[(x, y)] = enhance(x, y)
    spots = new.copy()
    if not i % 10:
        print(i)
    if i == 1:
        t = 0
        for x, y in spots:
            if spots[(x, y)] and 95 <= x <= 305 and 95 <= y <= 305:
                t += 1

t2 = 0
for x, y in spots:
    if spots[(x, y)] and 95 <= x <= 305 and 95 <= y <= 305:
        t2 += 1

print(f'Part 1: {t}\nPart 2: {t2}')
