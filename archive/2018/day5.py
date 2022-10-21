with open('day5.txt') as file:
    data = file.readline()

destroy = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    destroy += [char+char.upper(), char.upper()+char]


def simplify(inp):
    last = ''
    while last != inp:
        last = inp
        for string in destroy:
            inp = inp.replace(string, '')
    return inp


print(len(simplify(data)))
stringLen = []
for char in alphabet:
    testCase = data.replace(char, '').replace(char.upper(), '')
    stringLen.append(len(simplify(testCase)))
print(min(stringLen))
