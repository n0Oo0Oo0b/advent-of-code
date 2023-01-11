from itertools import cycle

import numpy as np
from time import perf_counter

st = perf_counter()

stack = np.zeros((7, 3500), bool)
stack[:, 0] = True

wind = open('../temp/input.txt').read().rstrip()
wind_it = cycle(enumerate(1 if i == '>' else -1 for i in wind))

rocks = [
    np.array([[1], [1], [1], [1]], bool),
    np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], bool),
    np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]], bool),
    np.array([[1, 1, 1, 1]], bool),
    np.array([[1, 1], [1, 1]], bool)
]

rocks_it = cycle(enumerate(rocks))


def collide(rock, x, y):
    w, h = rock.shape
    return (rock & stack[x:x+w, y-h+1:y+1]).any()


def top_stack_state():
    return tuple(np.nonzero(i)[0][-1] for i in stack)


seen_states = {}
step = 0
while step < 2022:
    # Add rock
    r_i, rock = next(rocks_it)
    w, h = rock.shape
    x, y = 2, np.nonzero(stack.any(axis=0))[0][-1] + h + 3
    while True:
        max_x = 7 - w
        w_i, direction = next(wind_it)
        if 0 <= (x+direction) <= max_x:
            if not collide(rock, x+direction, y):
                x += direction
        if not collide(rock, x, y-1):
            y -= 1
        else:
            stack[x: x+w, y-h+1:y+1] |= rock
            break
    step += 1

print(np.nonzero(stack.any(axis=0))[0][-1])

et = perf_counter()
print(f"{(et - st) * 1000:.2f}ms")
