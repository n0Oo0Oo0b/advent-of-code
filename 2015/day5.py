import re

def is_nice_1(string):
    if re.findall(r'ab|cd|pq|xy', string): return False
    elif not re.findall(r'(\w)\1', string): return False
    elif len(re.findall(r'[aeiou]', string)) < 3: return False
    return True

def is_nice_2(string):
    if not re.findall(r'(\w\w).*?\1', string): return False
    elif not re.findall(r'(\w).\1', string): return False
    return True


def day5(data):
    nice_1, nice_2 = 0, 0
    for row in data.splitlines():
        if is_nice_1(row):
            nice_1 += 1
        if is_nice_2(row):
            nice_2 += 1
    return nice_1, nice_2

if __name__ == '__main__':
    with open('inputs/day5.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day5(data)))

# print(day5('ugknbfddgicrmopn'))
