from itertools import combinations


def day17(inp):
    data = sorted(int(i) for i in inp.splitlines())
    print(data)
    # calculate upper and lower bound for container count
    max_containers = 0
    while sum(data[:max_containers]) < 150:
        max_containers += 1
    min_containers = 1
    while sum(data[-min_containers:]) < 150:
        min_containers += 1

    # Brute force
    part1 = 0
    min_possible = None
    part2 = 0
    for num_containers in range(min_containers, max_containers + 1):
        for combination in combinations(data, num_containers):
            if sum(combination) != 150:
                continue
            part1 += 1
            if not min_possible:
                min_possible = num_containers
            if num_containers == min_possible:
                part2 += 1

    return part1, part2


if __name__ == '__main__':
    with open('inputs/day17.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day17(data)))
