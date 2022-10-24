def day1(data):
    floor = 0
    part2 = None
    for i, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1
            if floor < 0 and part2 is None:
                part2 = i+1
    return floor, part2


if __name__ == '__main__':
    with open('inputs/day1.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day1(data)))
