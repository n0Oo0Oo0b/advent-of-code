import re


correct = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def validate(k, v, part2=False):
    if part2:
        if k in ('cats', 'trees'):
            if correct[k] < v:
                return True
        elif k in ('pomeranians', 'goldfish'):
            if correct[k] > v:
                return True
    return correct[k] == v

with open('day16.txt') as file:
    data = file.read().split('\n')

for row in data:
    sue, _, qualities = row.partition(': ')
    for i in qualities.split(', '):
        k, _, v = i.partition(': ')
        if not validate(k, int(v)):  # pass in True for part 2
            break
    else:
        print(sue)
        break
