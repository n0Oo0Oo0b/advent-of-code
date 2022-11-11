from itertools import product

import numpy as np


def step(current):
    padded = np.pad(current, 1)
    def surrounding(x, y):
        x += 1  # account for padding offset
        y += 1  #
        total = -padded[x, y].astype(int)  # subtract current location first
        for dx, dy in product(range(-1, 2), repeat=2):
            total += padded[x + dx, y + dy]  # add with offset
        return total
    surround = np.fromfunction(  # numpy magic
        surrounding,
        current.shape,
        dtype=int
    )
    return (surround == 3) | (current & (surround == 2))


def day18(inp):
    CORNER_POSITIONS = (0, 0, -1, -1), (0, -1, 0, -1)
    # Process input
    data = np.array([[char == '#' for char in line] for line in inp.splitlines()], bool)
    grid_1 = data.copy()  # part 1
    grid_2 = data.copy()  # part 2
    grid_2[CORNER_POSITIONS] = True  # always on light
    for _ in range(100):
        # Part 1
        grid_1 = step(grid_1)
        # Part 2
        grid_2 = step(grid_2)
        grid_2[CORNER_POSITIONS] = True
    return grid_1.sum(), grid_2.sum()


if __name__ == '__main__':
    with open('inputs/day18.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day18(data)))
