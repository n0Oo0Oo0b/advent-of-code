import re


def day10(data):
    def say(match):
        return f'{match.end() - match.start()}{match.string[match.start()]}'

    for _ in range(40):
        data = re.sub(r'(\d)\1*', say, data)
    part1 = len(data)
    for _ in range(10):
        data = re.sub(r'(\d)\1*', say, data)
    return part1, len(data)


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day10(data)))
