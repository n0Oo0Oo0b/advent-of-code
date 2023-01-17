import re
from string import ascii_lowercase


def solution(inp):
    part1 = 0
    part2 = None
    for line in inp.splitlines():
        name, sector_id, checksum = re.search(r'([a-z-]+)-(\d+)\[(.{5})]', line).groups()
        sector_id = int(sector_id)
        correct_checksum = ''.join(sorted(ascii_lowercase, key=lambda x: (-name.count(x), x))[:5])
        if checksum != correct_checksum:
            continue
        part1 += sector_id
        result = ''
        for char in name:
            if char in ascii_lowercase:  # skip '-'
                char = ascii_lowercase[(ascii_lowercase.find(char) + sector_id) % 26]
            result += char
        if result == 'northpole-object-storage':
            part2 = sector_id
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
