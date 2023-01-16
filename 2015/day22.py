import re
from collections import namedtuple


_Effect = namedtuple('Effect', ['cost', 'duration', 'damage', 'health', 'armor', 'mana'], defaults=[1, 0, 0, 0, 0])

# noinspection PyArgumentList
_spells = [
    _Effect(53, damage=4),
    _Effect(73, damage=2, health=2),
    _Effect(113, 6, armor=7),
    _Effect(173, 6, damage=3),
    _Effect(229, 5, mana=101)
]


def _solve(hp, mana, boss_hp, boss_dmg, part2, player_turn=True, effects=None, mana_spent=0, min_mana=1e99):
    if effects is None:
        effects = {}
    if player_turn and part2:
        # noinspection PyArgumentList
        effects[_Effect(0, 1, health=-1)] = 1
    # Effects
    armor = 0
    new_effects = {}
    for effect, duration in effects.items():
        _, _, e_dmg, e_hp, e_armor, e_mana = effect
        boss_hp -= e_dmg
        hp += e_hp
        armor += e_armor
        mana += e_mana
        duration -= 1
        if duration > 0:
            new_effects[effect] = duration
    effects = new_effects
    # End branch
    if mana_spent >= min_mana:
        return 1e99
    elif hp <= 0:
        return 1e99
    if boss_hp <= 0:
        return mana_spent
    # Continue
    if player_turn:
        for spell in _spells:
            if mana < spell.cost or spell in effects:
                continue
            n_mana_spent = mana_spent + spell.cost
            n_mana = mana - spell.cost
            n_effects = effects.copy()
            n_effects[spell] = spell.duration
            r = _solve(hp, n_mana, boss_hp, boss_dmg, part2, False, n_effects, n_mana_spent, min_mana)
            min_mana = min(min_mana, r)
        return min_mana
    else:
        hp -= max(1, boss_dmg - armor)
        return _solve(hp, mana, boss_hp, boss_dmg, part2, True, effects, mana_spent, min_mana)


def day22(inp):
    boss_hp, boss_dmg = (int(i) for i in re.findall(r'\d+', inp))
    part1 = _solve(50, 500, boss_hp, boss_dmg, False)
    part2 = _solve(50, 500, boss_hp, boss_dmg, True)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day22(data)))
