import re

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
requirements = {i: set() for i in ALPHABET}

with open('day7.txt') as file:
    for line in file.read().split('\n'):
        d = re.findall(r'Step (.) must be finished before step (.) can begin\.', line)[0]
        requirements[d[1]].add(d[0])


def getPossible():
    return [i for i in requirements if not (requirements[i].difference(completed) or i in completed)]


completed = []

while len(completed) < 26:
    step = getPossible()[0]
    completed.append(step)
print(''.join(completed))


def getTime(letter):
    return 61 + ALPHABET.index(letter)


completed = []
tasks = [('', 0)]*5
tick = 0
while tick := tick+1:
    for i, task in enumerate(tasks):
        if tick > getTime(task[0]) + task[1]:
            tasks[i] = ('', tick)
        
        if not task[0]:
            pass
