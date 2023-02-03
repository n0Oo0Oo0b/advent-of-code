import numpy as np
import re

from aoc_helper.utils import decode_text


def solution(inp):
    screen = np.zeros((6, 50), bool)
    for line in inp.splitlines():
        a, b = (int(num) for num in re.findall(r'\d+', line))
        if line.startswith('rect'):
            screen[:b, :a] = True
        else:
            if line.startswith('rotate column'):
                screen[:, a] = np.roll(screen[:, a], b)
            else:
                screen[a, :] = np.roll(screen[a, :], b)
    return screen.sum(), decode_text(screen.tolist())  # type: ignore


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
