from itertools import product
import numpy as np

with open('day18.txt') as file:
    data = np.array([[i=='#' for i in line] for line in file.read().splitlines()], bool)

board_size = data.shape[0]
grid = np.pad(data, 1)

def output(grid):
    for i in grid:
        print(''.join('#' if j else '.' for j in i))
    print('\n')

for _ in range(100):
    grid[1,(1,-2)] = grid[-2,(1,-2)] = True
    new = grid.copy()
    for x, y in product(range(1, board_size+1), repeat=2):
        on = grid[x,y]
        surround_count = grid[x-1:x+2,y-1:y+2].sum() - on
        if on:
            new[x,y] = surround_count in (2, 3)
        else:
            new[x,y] = surround_count == 3
    grid = new
    # output(grid[1:-1,1:-1])  # 

grid[1,(1,-2)] = grid[-2,(1,-2)] = True
print(grid.sum())
