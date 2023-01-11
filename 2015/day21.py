from math import ceil, inf
from collections import namedtuple
from dataclasses import dataclass
from itertools import chain, combinations, product


_Item = namedtuple('Item', ('price', 'damage', 'defense'), defaults=(0, 0))


@dataclass
class _Stats:
    health: int = 100
    damage: int = 0
    defense: int = 0
    price: int = 0

    @classmethod
    def get_stats(cls, *items):
        stats = cls()
        for item in items:
            stats.damage += item.damage
            stats.defense += item.defense
            stats.price += item.price
        return stats

    def __hash__(self):
        # Ignores price
        return hash((self.health, self.damage, self.defense))


def day21(inp):
    # Parse input
    BOSS = _Stats(*(int(i.split()[-1]) for i in inp.splitlines()))
    # Setup shop
    WEAPONS = [_Item(price, damage=damage) for price, damage in [
        (8, 4), (10, 5), (25, 6), (40, 7), (74, 8)
    ]]
    ARMOR = [_Item(price, defense=defense) for price, defense in [
        (0, 0), (13, 1),(31, 2), (53, 3), (75, 4), (102, 5)
    ]] + [_Item(0, 0, 0)]  # Null armor
    ARTIFACTS = [_Item(*i) for i in [
        (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)
    ]]

    # Solve
    min_win = inf  # Part 1
    max_lose = 0  # Part 2
    seen_results = {}
    artifact_combinations = chain(*(combinations(ARTIFACTS, i) for i in range(3)))
    for weapon, armor, artifacts in product(WEAPONS, ARMOR, artifact_combinations):  # Brute force
        stats = _Stats.get_stats(weapon, armor, *artifacts)
        # Find win/loss
        if stats in seen_results:
            # Already calculated for given stats
            win = seen_results[stats]
        else:
            # Calculate
            turns_player = ceil(BOSS.health / max(1, stats.damage - BOSS.defense))
            turns_boss = ceil(stats.health / max(1, BOSS.damage - stats.defense))
            win = turns_player <= turns_boss
            seen_results[stats] = win
        # Update min/max
        if win:
            min_win = min(min_win, stats.price)
        else:
            max_lose = max(max_lose, stats.price)
    return min_win, max_lose


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day21(data)))
