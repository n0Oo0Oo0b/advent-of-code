import numpy as np
import re

def day6(data):
    lights = np.zeros((1000, 1000), bool)  # part 1
    lights2 = np.zeros((1000, 1000), int)  # part 2
    for row in data.splitlines():
        x1, y1, x2, y2 = (int(i) for i in re.findall(r'\d+', row))  # parse numbers
        area = lights[x1:x2+1, y1:y2+1]
        area2 = lights2[x1:x2+1, y1:y2+1]
        if row.startswith('turn on'):
            area[:] = True
            area2[:] += 1
        elif row.startswith('turn off'):
            area[:] = False
            area2[:] -= 1
            np.clip(area2, 0, np.inf, out=area2)  # remove negative brightness
        else:
            area[:] = ~area
            area2[:] += 2
    return lights.sum(), lights2.sum()


if __name__ == '__main__':
    with open('inputs/day6.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day6(data)))
