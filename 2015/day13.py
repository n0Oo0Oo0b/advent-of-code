from collections import defaultdict
from itertools import permutations
import re


def _max_happiness(people, happiness_pairs):
    # Brute force all arrangements
    max_ = 0
    for c in permutations(people):
        happiness = 0
        for i in range(len(c)):
            happiness += happiness_pairs[frozenset((c[i],c[i-1]))]
        max_ = max(max_, happiness)
    return max_


def day13(data):
    # Parse data into dict of {frozenset(name1, name2) : net_happiness}
    net_happiness = defaultdict(int)
    people = set()
    for line in data.split('\n'):
        # Regex match useful information
        r = re.match(r'^(\w+) .* (gain|lose) (\d+) .* (\w+)\.', line)
        if r is None: raise ValueError
        # Process information
        a, sign, value, b = r.groups()
        value = int(value) * (1 if sign == 'gain' else -1)
        net_happiness[frozenset((a, b))] += value
        people |= {a, b}
    # Run brute force
    part1 = _max_happiness(people, net_happiness)
    people.add('you')
    part2 = _max_happiness(people, net_happiness)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day13(data)))
