from dataclasses import dataclass
from itertools import combinations_with_replacement
from math import prod
import re

@dataclass
class _Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    @property
    def stats(self):
        return (self.capacity, self.durability, self.flavor, self.texture, self.calories)

    def __mul__(self, other):
        return _Ingredient(*(i*other for i in self.stats))

    def __add__(self, other):
        return _Ingredient(*(i + j for i, j in zip(self.stats, other.stats)))

    @property
    def score(self):
        if any(i <= 0 for i in self.stats[:-1]):
            return 0
        return prod(self.stats[:-1])


def day15(data):
    # Parse input
    ingredients = []
    for row in data.splitlines():
        values = (int(i) for i in re.findall(r'-?\d+', row))
        ingredients.append(_Ingredient(*values))
    # Brute force every recipe
    part1 = 0
    part2 = 0
    for i in combinations_with_replacement(range(101), len(ingredients)-1):
        i = (0, *i, 100)
        quantities = (i[j+1] - i[j] for j in range(len(ingredients)))
        # Calculate ingredient score
        cookie = _Ingredient(0, 0, 0, 0, 0)  # start with empty stats
        for ingredient, multiplier in zip(ingredients, quantities):
            cookie += ingredient * multiplier
        score = cookie.score
        # Update maximum
        part1 = max(part1, score)
        if cookie.calories == 500:
            part2 = max(part2, cookie.score)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day15(data)))
