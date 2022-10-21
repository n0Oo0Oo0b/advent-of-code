import numpy as np

with open('day19.txt') as file:
    data = [i.replace('\n', '') for i in file.readlines()]


def getLocation(position):
    global data
    try:
        return data[position[1]][position[0]]
    except IndexError:
        return ' '


direction = np.array([0, 1])
position = np.array([data[0].index('|'), 0])

steps = 0
passed = []
while True:
    while getLocation(position) != '+':
        steps += 1
        position += direction
        if getLocation(position) == ' ':
            print(''.join(passed))
            print(steps)
            exit(0)
        elif getLocation(position) not in ('|', '-', '+'):
            passed.append(getLocation(position))
    rD = np.array(tuple(reversed(direction)))
    if getLocation(position + rD) != ' ':
        direction = rD
    else:
        direction = -rD

    steps += 1
    position += direction
