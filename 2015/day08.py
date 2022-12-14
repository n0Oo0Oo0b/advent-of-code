import re


def day08(data):
    part1 = 0
    part2 = 0
    for line in data.splitlines():
        # Escape sequences go brrr
        part1 += sum(len(i)-1 for i in re.findall(r'\\\"|\\\\|\\x..', line)) + 2
        part2 += line.count('\\') + line.count('"') + 2
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day08(data)))
