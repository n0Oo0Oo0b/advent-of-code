from collections import namedtuple
from itertools import combinations, product
from math import ceil, inf

Entity = namedtuple('Entity', ('health', 'damage', 'armor'))
Item = namedtuple('Item', ('price', 'damage', 'defense'))

BOSS = Entity(health=100, damage=8, armor=2)  # input here

SHOP = [Item(*i) for i in [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]]

WEAPONS = SHOP[0:5]
ARMORS = SHOP[5:10] + [Item(0, 0, 0)]
RINGS = SHOP[10:]


def win(player):
    turns_player = ceil(BOSS.health / max(1, player.damage - BOSS.armor))
    turns_boss = ceil(player.health / max(1, BOSS.damage - player.armor))
    return turns_player <= turns_boss

def add_stats(*items):
    stats = [0, 0, 0]
    for item in items:
        for i, value in enumerate(item):
            stats[i] += value
    return Item(*stats)

min_cost = inf
max_cost = 0
for weapon, armor in product(WEAPONS, ARMORS):
    kit = add_stats(weapon, armor)
    if kit.price >= min_cost:
        continue

    for ring_count in range(3):
        for i in combinations(RINGS, ring_count):
            new = add_stats(kit, *i)
            if win(Entity(100, new.damage, new.defense)):
                min_cost = min(min_cost, new.price)
            else:
                max_cost = max(max_cost, new.price)

# Finally I can do both parts at once
print(min_cost)
print(max_cost)
