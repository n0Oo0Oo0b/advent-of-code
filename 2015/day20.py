from math import ceil
import numpy as np


def day20(inp):  # still can probably be improved
    inp = int(inp)
    # Part 1
    target = ceil(inp/10)
    presents = np.zeros((target+1,), int)  # presents[n] = number of presents at house n
    for n in range(1, target+1):
        presents[::n] += n
    part1 = np.nonzero(presents > target)[0][1]
    # Part 2
    target = ceil(inp/11)
    presents.fill(0)  # reset present count
    for n in range(1, target+1):
        presents[:n*50:n] += n
    part2 = np.nonzero(presents > target)[0][1]
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    from time import perf_counter
    st = perf_counter()
    print("Part 1: {}\nPart 2: {}".format(*day20(data)))
    et = perf_counter()
    print(f'Completed in {et - st:.3f}s')
