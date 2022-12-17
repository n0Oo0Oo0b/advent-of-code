from itertools import cycle

import numpy as np
from time import perf_counter

st = perf_counter()

stack = np.zeros((7, 200), bool)
stack[:, 0] = True

wind = open(0).read().rstrip()
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
    region = stack[x:x+w, y-h+1:y+1]
    return (rock & region).any()


def top_stack_state():
    return tuple(np.nonzero(i)[0][-1] for i in stack)


seen_states = {}
state_heights = [0]
removed_t = 0
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
    # Track state
    step += 1
    remove: int = min(np.nonzero(i)[0][-1] for i in stack)
    if remove:
        stack[:, 1:-remove] = stack[:, 1+remove:]
        stack[:, -remove:] = False
        removed_t += remove
    top = np.nonzero(stack.any(axis=0))[0][-1]
    state_heights.append(top + removed_t)
    # state = (r_i, w_i, top_stack_state())
    # if r0 := seen_states.get(state):
    #     r1 = step
    #     # break
    # else:
    #     seen_states[state] = step

# delta_steps = r1 - r0
# delta_heights = state_heights[r1] - state_heights[r0]
#
# print(r0, state_heights[r0], delta_steps)
#
# # Before cycle
# total_height = state_heights[r0]
# steps_remaining = int(1e12) - r0
#
# # Integer cycles
# cycles, steps_remaining = divmod(steps_remaining, delta_steps)
# total_height += delta_heights * cycles
#
# # Remaining
# total_height += state_heights[r0 + steps_remaining] - state_heights[r0]

print(state_heights[2022])

et = perf_counter()
print(f"{(et - st) * 1000:.2f}ms")

# 1725
# 317 477
# 2042 3171
