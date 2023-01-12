from collections import defaultdict
import re


def day19(inp):
    # Parse input
    raw_conversions, _, chemical = inp.partition('\n\n')
    conversions = defaultdict(list)  # maps reactant to products
    reductions = {}  # maps product to reactant
    for line in raw_conversions.splitlines():
        reactant, _, product = line.partition(' => ')
        conversions[reactant].append(product)
        reductions[product] = reactant
    # Part 1
    possible_next = set()
    for reactant, products in conversions.items():
        for m in re.finditer(reactant, chemical):
            start, end = m.span()
            for product in products:
                possible_next.add(chemical[:start] + product + chemical[end:])
    part1 = len(possible_next)
    # Part 2
    pattern = re.compile(fr'.*({"|".join(reductions)})')  # pattern to find rightmost replacement
    part2 = 0
    while chemical != 'e':
        m = re.match(pattern, ''.join(chemical))
        (start, end), group = m.span(1), m.group(1)
        chemical = chemical[:start] + reductions[group] + chemical[end:]
        part2 += 1
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day19(data)))
