import re


def day25(inp):
    y, x = map(int, re.findall(r'\d+', inp))
    num_steps = ((x+y)**2 - x - 3*y) // 2  # magic formula
    num_steps %= 16777196  # magic number (cycle repeat length)
    n = 20151125
    for _ in range(num_steps):
        n = (n * 252533) % 33554393
    return n


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}".format(day25(data)))
