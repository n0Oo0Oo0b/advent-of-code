def _get_locations(directions):
    x, y = 0, 0
    visited = {(x, y)}
    for char in directions:
        if char == '<': x -= 1
        elif char == '>': x += 1
        elif char == '^': y += 1
        elif char == 'v': y -= 1
        visited.add((x, y))  # type: ignore
    return visited


def day03(data):
    part1 = len(_get_locations(data))
    part2 = len(_get_locations(data[::2]) | _get_locations(data[1::2]))
    return part1, part2


if __name__ == '__main__':
    with open('inputs/day03.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day03(data)))
