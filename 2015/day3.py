def part1(data):
    visited = {(0,0)}
    x, y = 0, 0
    for char in data:
        if char == '<': x -= 1
        elif char == '>': x += 1
        elif char == '^': y -= 1
        else: y += 1
        visited.add((x, y))
    return len(visited)

def part2(data):
    # this is kinda repetitive but whatever
    visited = {(0,0)}
    santa = [0,0]
    robosanta = [0,0]
    for i, char in enumerate(data):
        move = santa if i%2==0 else robosanta
        if char == '<': move[0] -= 1
        elif char == '>': move[0] += 1
        elif char == '^': move[1] -= 1
        else: move[1] += 1
        visited.add(tuple(move))
    return len(visited)

def day3(data):
    return part1(data), part2(data)


if __name__ == '__main__':
    with open('inputs/day3.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day3(data)))
