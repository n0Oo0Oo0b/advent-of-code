import numpy as np
import re


def day14(data: str):
    lines = data.splitlines()
    distances = np.empty((len(lines), 2503), int)
    for i, line in enumerate(lines):
        # Parse input
        speed, stamina, cooldown = (int(i) for i in re.findall(r'\d+', line))
        # Calculate distance at x
        reindeer_distance = []
        current_distance = 0
        while len(reindeer_distance) < 2503:
            current_distance += speed
            # Move reindeer
            reindeer_distance.extend(range(current_distance, current_distance+speed*stamina, speed))
            current_distance = reindeer_distance[-1]
            # Cooldown
            reindeer_distance += [current_distance] * cooldown
        # Slice out extra values, add to array
        distances[i] = reindeer_distance[:2503]
    first = (distances == distances.max(axis=0))  # find the reindeer(s) that were furthest
    return max(distances[:,-1]), max(first.sum(axis=1))


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day14(data)))
