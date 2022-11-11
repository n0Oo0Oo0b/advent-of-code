import numpy as np
import re


def day6(data):
    lights_1 = np.zeros((1000, 1000), bool)  # part 1
    lights_2 = np.zeros((1000, 1000), int)  # part 2
    for row in data.splitlines():
        # Parse row
        x1, y1, x2, y2 = (int(i) for i in re.findall(r'\d+', row))
        area_1 = lights_1[x1:x2+1, y1:y2+1]
        area_2 = lights_2[x1:x2+1, y1:y2+1]
        # Apply instruction
        if row.startswith('turn on'):
            area_1[:] = True
            area_2[:] += 1
        elif row.startswith('turn off'):
            area_1[:] = False
            area_2[:] -= 1
            np.clip(area_2, 0, np.inf, out=area_2)  # constrain negative values
        elif row.startswith('toggle'):
            area_1[:] = ~area_1
            area_2[:] += 2
    return lights_1.sum(), lights_2.sum()


if __name__ == '__main__':
    with open('inputs/day6.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day6(data)))
