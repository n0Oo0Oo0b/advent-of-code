with open('day12.txt') as file:
    data = [i.split('-') for i in file.read().split('\n')]

paths = {}
for a, b in data:
    if a not in paths:
        paths[a] = []
    if b not in paths:
        paths[b] = []
    paths[a].append(b)
    paths[b].append(a)


def doubleSmall(path):
    """
    Returns whether or not the path has visited a small cave more than once
    """
    c = {}
    for i in path:
        if i in c and i.islower():
            return True
        else:
            c[i] = True
    return False


def findPath(bonus, prevPath=None):
    """
    Finds all possible paths starting with prevPath to the end point
    :param bonus: Flag to indicate whether a single small cave can be visited twice
    :param prevPath:
    :return: list of all possible paths
    """
    if prevPath is None:
        prevPath = ['start']
    
    if prevPath[-1] == 'end':  # Path is already complete
        return [prevPath]
    
    # Generate all possible caves that can be searched next
    if bonus and not doubleSmall(prevPath):
        possibleNext = [i for i in paths[prevPath[-1]] if i != 'start']
    else:
        possibleNext = [i for i in paths[prevPath[-1]] if i.isupper() or i not in prevPath]
    
    # Recursively search all possible next caves
    possibles = []
    for i in possibleNext:
        possibles.extend(findPath(bonus, prevPath + [i]))
    
    return possibles


print(f'Part 1: {len(findPath(False))}\nPart 2: {len(findPath(True))}')
