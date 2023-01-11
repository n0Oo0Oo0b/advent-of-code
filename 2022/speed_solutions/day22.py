import numpy as np
import re

raw_map, route = open(0).read().split('\n\n')
max_l = max(len(i) for i in raw_map.splitlines())
M = np.array([list(i.ljust(max_l)) for i in raw_map.splitlines()])

pos = np.array((0, np.nonzero(M[0] != ' ')[0][0]), int)
direction = np.array((0, 1), int)


def step():
    global pos
    new_pos = pos.copy()
    new_pos = (new_pos + direction) % M.shape
    while M[*new_pos] == ' ':
        new_pos = (new_pos + direction) % M.shape
    if M[*new_pos] == '#':
        return False
    pos[:] = new_pos
    return True


def move(steps):
    for _ in range(steps):
        if not step():
            return


for i in re.findall(r'\d+|[LR]', route):
    if i == 'L':
        x, y = direction
        direction[:] = -y, x
    elif i == 'R':
        x, y = direction
        direction[:] = y, -x
    else:
        move(int(i))

print(direction)

print(pos + (1, 1))

#


import numpy as np
import re

c = {
    ' ': 0,
    '.': -1,
    '#': -2
}

raw_map, route = open(0).read().split('\n\n')
max_l = max(len(i) for i in raw_map.splitlines())
M = np.array([[c[j] for j in i.ljust(max_l)] for i in raw_map.splitlines()], int)
B = 50
M = np.pad(M, B)
# 0, 8 + B, B
# 50, 100
pos = np.array((50, 100))
D = [
    np.array((0, 1)),
    np.array((1, 0)),
    np.array((0, -1)),
    np.array((-1, 0))
]
direction = D[0].copy()


def edge(x, y, d, e):
    x += 1
    y += 1
    region = M[x * B:x * B + B, y * B:y * B + B]
    if d == 0:
        r = region[0]
    elif d == 1:
        r = region[:, -1]
    elif d == 2:
        r = region[-1][::-1]
    else:
        r = region[:, 0][::-1]
    return r[::-1] if e else r


n = 1


def link(a, b):
    global n
    edge(*a)[:] = edge(*b)[:] = range(n, n + B)
    n += B


# link((0,1,1,1),(0,1,2,0))
# link((0,0,2,1),(-1,2,2,0))
# link((2,1,0,1),(2,1,1,0))
# link((2,0,0,1),(3,2,0,0))
# link((1,-1,1,0),(3,3,0,1))
# link((0,3,3,1),(2,4,3,0))
# link((1,3,3,0),(1,3,2,1))
link((1, 0, 2, 0), (1, 0, 1, 1))
link((0, 0, 1, 0), (2, -1, 1, 1))
link((-1, 1, 2, 0), (3, -1, 1, 1))
link((-1, 2, 2, 0), (4, 0, 0, 1))
link((1, 2, 3, 0), (1, 2, 0, 1))
link((3, 1, 3, 0), (3, 1, 0, 1))
link((2, 2, 3, 0), (0, 3, 3, 1))
print(str(M).replace(' 0', '  '))


def step():
    new_pos = pos.copy()
    new_pos = (new_pos + direction) % M.shape
    new_direction = direction.copy()
    if M[*new_pos] > 0:
        positions = [np.array(i) for i in zip(*np.nonzero(M == M[*new_pos]))]
        if len(positions) == 1:
            p = positions[0]
        else:
            p = next(filter(lambda x: not (x == new_pos).all(), positions))
        for d in D:
            if ((p + d) == pos).all():
                continue
            if M[*(p + d)] < 0:
                new_pos = p + d
                new_direction = d
                break
    if M[*new_pos] == -2:
        return False
    pos[:] = new_pos
    direction[:] = new_direction
    return True


def move(steps):
    for _ in range(steps):
        if not step():
            return


for i in re.findall(r'\d+|[LR]', route):
    if i == 'L':
        x, y = direction
        direction[:] = -y, x
    elif i == 'R':
        x, y = direction
        direction[:] = y, -x
    else:
        move(int(i))

r, c = pos - (B - 1, B - 1)
print(r, c, np.nonzero((D == direction).all(axis=1))[0][0])

direction = np.array((0, 1), int)
