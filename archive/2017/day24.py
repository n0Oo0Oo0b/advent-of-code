with open('day24.txt') as file:
    data = [list(map(int, i.split('/'))) for i in file.read().split('\n')]


def getPossibleBridges(startPort, components):
    possible = []
    for component in components:
        if startPort in component:
            possible.append(component.copy())
    if not possible:
        return [startPort]
    
    print(possible)
    
    possibleBridges = []
    for i in possible:
        c = components.copy()
        c.remove(i)
        if i[0] == startPort:
            otherPort = i[1]
        else:
            otherPort = i[0]
        possibleBridges.extend([[i] + j for j in getPossibleBridges(otherPort, c)])
    return possibleBridges


print(getPossibleBridges(0, data))
