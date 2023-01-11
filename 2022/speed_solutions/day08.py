import numpy as np
from aocd import lines as inp


data = np.array([[int(i) for i in line] for line in inp])

s_x, s_y = data.shape

part1 = 0
part2 = 0
for x in range(s_x):
    for y in range(s_y):
        current = data[x, y]
        adj = data[x, :y][::-1], data[x, y+1:], data[:x, y][::-1], data[x+1:, y]
        visible = False
        scenery = 1
        for trees in adj:
            if (trees < current).all():
                visible = True
            i = -1
            for i in range(len(trees)):
                if trees[i] >= current:
                    break
            scenery *= i + 1
        if visible:
            part1 += 1
        if scenery > part2:
            part2 = scenery

print(part1, part2)
