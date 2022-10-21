from collections import defaultdict
import re

inf = float('inf')


class DamageType:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.other == self.name


class Group:
    immuneGroup = True
    groupId = 1
    
    def __init__(self, unitCount=0, hp=0, damage=0, initiative=0, atkType='', immunities=None, weaknesses=None):
        if immunities is None:
            immunities = []
        if weaknesses is None:
            weaknesses = []
        
        self.immuneGroup = Group.immuneGroup
        self.groupId = Group.groupId
        Group.groupId += 1
        self.selected, self.target = False, None
        
        self.unitCount, self.hp = unitCount, hp
        self.damage, self.atkType = damage, atkType
        self.initiative = initiative
        
        self.multipliers = defaultdict(lambda: 1)
        for i in immunities:
            self.multipliers[i] = 0
        for i in weaknesses:
            self.multipliers[i] = 2
    
    def __str__(self):
        return f'{"Immune system" if self.immuneGroup else "Infection"} group {self.groupId} ' \
               f'({self.unitCount} / {self.hp} / {self.damage} / {self.initiative})'
    
    def __int__(self):  # Returns remaining health
        return self.unitCount * self.hp
    
    def __abs__(self):  # Returns effective damage
        return self.unitCount * self.damage
    
    def __bool__(self):
        return self.unitCount > 0
    
    def calculateDamage(self, damage, damageType):
        return self.multipliers[damageType] * damage
    
    def takeDamage(self, damage, damageType):
        print(self.unitCount)
        unitsLost = self.calculateDamage(damage, damageType) // self.hp
        print(self, damage, unitsLost, self.hp)
        self.unitCount -= unitsLost
        if self.unitCount < 0:
            self.unitCount = 0
        print(self.unitCount)
    
    def dealDamage(self):
        damage = self.unitCount * self.damage
        self.target.takeDamage(damage, self.atkType)
    
    def selectTarget(self, others):
        others = list(filter(lambda x: not x.selected, others))
        currentMax = (0, inf, inf)
        maxIndex = -1
        for i, group in enumerate(others):
            effectiveDamage = group.calculateDamage(self.damage, self.atkType)
            score = (effectiveDamage, abs(group), group.initiative)
            if score > currentMax:
                currentMax = score
                maxIndex = i
        if maxIndex == -1:
            return None
        target = others[maxIndex]
        target.selected = True
        self.target = target
        return target
    
    def clearTarget(self):
        self.target.selected = False
        self.target = None


def parse(line):
    values = list(map(int, re.findall(r'\d+', line)))
    atkType = re.findall(r'\d+ (?!units|hit)(\w+)', line)[0]
    immune = m[0].split(', ') if (m := re.findall(r'immune to (.*?)[);]', line)) else None
    weak = m[0].split(', ') if (m := re.findall(r'weak to (.*?)[);]', line)) else None
    return Group(*values, atkType, immune, weak)


with open('day24.txt') as file:
    immuneSystem, infection = file.read().split('\n\n')
    
Group.immuneGroup, Group.groupId = True, 1
immuneSystem = list(map(parse, immuneSystem.splitlines()[1:]))

Group.immuneGroup, Group.groupId = False, 1
infection = list(map(parse, infection.splitlines()[1:]))

while any(immuneSystem) and any(infection):
    allGroups = immuneSystem + infection
    
    allGroups.sort(key=lambda x: (abs(x), x.initiative), reverse=True)
    for group in allGroups:
        group.selectTarget(infection if group.immuneGroup else immuneSystem)
    
    allGroups.sort(key=lambda x: x.initiative)
    for group in allGroups:
        if group.target:
            print(group)
            group.dealDamage()
            group.clearTarget()
            print('\n')
    
    break
