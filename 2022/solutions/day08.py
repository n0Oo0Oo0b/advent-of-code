from itertools import product
import numpy as np


def solve(inp):
    data = np.array([list(i) for i in inp.splitlines()], dtype=int)
    part1 = 0
    part2 = 0
    width, height = data.shape
    for x, y in product(range(width), range(height)):
        current = data[x, y]
        directions = (
            data[x, y+1:],  # down
            data[x, :y][::-1],  # up
            data[x+1:, y],  # right
            data[:x, y][::-1]  # left
        )
        # Calculate
        visible = False
        scenery = 1
        for trees in directions:
            # Visible from edge (part 1)
            if (trees < current).all():
                visible = True
            # Scenery value
            for count, tree in enumerate(trees, start=1):
                if tree >= current:
                    break
            scenery *= count
        # Update
        if visible:
            part1 += 1
        part2 = max(part2, scenery)

    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
