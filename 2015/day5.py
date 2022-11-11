import re


def _is_nice_1(string):
    if re.findall(r'ab|cd|pq|xy', string):  # illegal sequences
        return False
    elif not re.findall(r'(\w)\1', string):  # repeat letter
        return False
    elif len(re.findall(r'[aeiou]', string)) < 3:  # 3+ vowels
        return False
    return True


def _is_nice_2(string):
    if not re.findall(r'(\w\w).*?\1', string):  # repeat sequence
        return False
    elif not re.findall(r'(\w).\1', string):  # xyx
        return False
    return True


def day5(data):
    nice_1 = 0  # Part 1
    nice_2 = 0  # Part 2
    for row in data.splitlines():
        if _is_nice_1(row):
            nice_1 += 1
        if _is_nice_2(row):
            nice_2 += 1
    return nice_1, nice_2


if __name__ == '__main__':
    with open('inputs/day5.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day5(data)))
