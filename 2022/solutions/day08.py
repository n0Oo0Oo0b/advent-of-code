import numpy as np


def speedcode_solution(inp):
    data = np.array([[int(i) for i in line] for line in inp.splitlines()])

    s_x, s_y = data.shape

    part1 = 0
    part2 = 0
    for x in range(s_x):
        for y in range(s_y):
            current = data[x, y]
            adj = data[x, :y][::-1], data[x, y+1:], data[:x, y][::-1], data[x+1:, y]
            visible = False
            scenery = 1
            for trees in adj:
                if (trees < current).all():
                    visible = True
                i = -1
                for i in range(len(trees)):
                    if trees[i] >= current:
                        break
                scenery *= i + 1
            if visible:
                part1 += 1
            if scenery > part2:
                part2 = scenery

    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = speedcode_solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
