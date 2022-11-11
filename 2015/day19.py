from collections import defaultdict
import re


def _parse_chemicals(inp):
    return re.split(r'(?=[A-Z])', inp)[1:]


def _part1(conversions, chemical):
    possible = set()
    for i, element in enumerate(chemical):
        for result in conversions[element]:
            r = ''.join(chemical[:i] + result + chemical[i+1:])
            possible.add(r)
    return len(possible)


def day19(inp):
    raw_conversions, _, chemical = inp.partition('\n\n')
    conversions = defaultdict(list)
    for line in raw_conversions.splitlines():
        reactant, _, product = line.partition(' => ')
        conversions[reactant].append(_parse_chemicals(product))
    chemical = _parse_chemicals(chemical)
    return _part1(conversions, chemical)


if __name__ == '__main__':
    with open('inputs/day19.txt') as file:
        data = file.read()
    print("Part 1: {}".format(day19(data)))
