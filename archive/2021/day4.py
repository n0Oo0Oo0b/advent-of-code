import numpy as np  # yes, i use numpy
import numpy.ma as ma
from itertools import product

# Import puzzle input
with open('day4.txt') as file:
    data = file.read().split('\n\n')

# Parse data (used to be 10+ lines long)
numbers = [int(i) for i in data[0].split(',')]
cards = [np.array([[j for j in i.split(' ') if j] for i in d.split('\n')], int) for d in data[1:]]


def getRemainingSum(grid, marked):  # Returns the sum of unmarked numbers using numpy masks
    return ma.masked_array(grid, marked).sum()


def runBingo(grid):  # Simulates the bingo card and returns tuple (nth card drawn, score)
    checks = np.zeros((5, 5), bool)
    for i, number in enumerate(numbers):
        
        for x, y in product(range(5), repeat=2):  # Mark number
            if grid[x, y] == number:
                checks[x, y] = True
        
        for x in range(5):  # Check for wins
            if checks[x].all() or np.rot90(checks)[x].all():
                return i, number * getRemainingSum(grid, checks)


# Run the solution on puzzle input
winTimes = [runBingo(i) for i in cards]
print(f'Part 1: {min(winTimes)[1]}\nPart 2: {max(winTimes)[1]}')
