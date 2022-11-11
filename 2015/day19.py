from collections import defaultdict
import re


def parse_chemicals(inp):
    return re.split(r'(?=[A-Z])', inp)[1:]


def _part1(conversions, chemical):
    pass


def day19(inp):
    raw_conversions, _, chemical = inp.partition('\n\n')
    conversions = defaultdict(list)
    for line in raw_conversions.splitlines():
        reactant, _, product = line.partition(' => ')
        conversions[reactant].append(parse_chemicals(product))
    chemicals = parse_chemicals(chemical)
    _part1(conversions, chemical)


if __name__ == '__main__':
    with open('inputs/day19.txt') as file:
        data = file.read()
    print(day19(data))
