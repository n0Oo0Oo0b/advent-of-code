from itertools import product
import numpy as np


def _step(current):
    padded = np.pad(current, 1)  # Pad to prevent IndexError on edge lights
    def surrounding(x, y):
        x += 1  # Account for padding offset
        y += 1  #
        total = -padded[x, y].astype(int)  # Subtract current location first
        for dx, dy in product(range(-1, 2), repeat=2):
            total += padded[x + dx, y + dy]  # Add with offset
        return total
    surround = np.fromfunction(  # numpy magic
        surrounding,
        current.shape,
        dtype=int
    )
    return (surround == 3) | (current & (surround == 2))  # more numpy magic


def day18(inp):
    CORNER_POSITIONS = (0, 0, -1, -1), (0, -1, 0, -1)  # x and y values
    # Process input
    data = np.array([[char == '#' for char in line] for line in inp.splitlines()], bool)
    grid_1 = data.copy()  # Part 1
    grid_2 = data.copy()  # Part 2
    grid_2[CORNER_POSITIONS] = True  # Always on light
    for _ in range(100):
        # Part 1
        grid_1 = _step(grid_1)
        # Part 2
        grid_2 = _step(grid_2)
        grid_2[CORNER_POSITIONS] = True  # Always on light
    return grid_1.sum(), grid_2.sum()


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day18(data)))
