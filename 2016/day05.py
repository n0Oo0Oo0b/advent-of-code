from hashlib import md5


def solution(inp):
    x = 0
    part1 = ''
    part2 = [''] * 8
    while len(part1) < 8 or not all(part2):
        hash_ = md5((inp + str(x)).encode('utf-8')).hexdigest()
        x += 1
        if not hash_.startswith('0'*5):
            continue
        # Part 1
        if len(part1) < 8:
            part1 += hash_[5]
        # Part 2
        if hash_[5] > '7':
            continue
        if not part2[i := int(hash_[5])]:
            part2[i] = hash_[6]
    return part1, ''.join(part2)


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
