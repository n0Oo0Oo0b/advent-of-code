import re

def say(match):
    return f'{match.end() - match.start()}{match.string[match.start()]}'

def day10(data):
    for _ in range(40):
        data = re.sub(r'(\d)\1*', say, data)
    part1 = len(data)
    for _ in range(10):  # burte force part 2 because I couldn't think of anything better
        data = re.sub(r'(\d)\1*', say, data)
    return part1, len(data)


if __name__ == '__main__':
    with open('inputs/day10.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day10(data)))
