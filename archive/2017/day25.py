import re

reg = {}
i = 0

functions = {}
nextFunction = ''


class State:
    def __init__(self, data):
        self.id = data[0]
        self.data = data[1:]
    
    def run(self):
        global reg, i, nextFunction, functions
        d = self.data
        if reg.setdefault(i, 0) == 0:
            c = d[:3]
        else:
            c = d[3:]
        reg[i] = int(c[0])
        if c[1] == 'l':
            i -= 1
        else:
            i += 1
        return functions[c[2]]


def parseFunction(data):
    global functions
    indexes = [9, 63, 93, 122, 176, 206, 235]  # 38, 151
    d = [data[i] for i in indexes]
    
    functions[d[0]] = state


with open('day25.txt') as file:
    rawData = file.read().replace('left', 'l').replace('right', 'r').split('\n\n')

for i in rawData[1:]:
    parseFunction(i)

for i, j in enumerate(rawData[1]):
    print(i, j)
