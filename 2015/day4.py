import hashlib


def day4(data):
    i = 0
    part1 = None
    part2 = None
    while part2 is None:
        hash_ = hashlib.md5((data + str(i)).encode('utf-8')).hexdigest()
        if hash_.startswith('0'*5):
            if part1 is None:
                part1 = i
            if hash_.startswith('0'*6):
                part2 = i
        i += 1
    return part1, part2


if __name__ == '__main__':
    with open('inputs/day4.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day4(data)))
