import re
import regex as re

with open('day7.txt') as file:
    data = [i.strip() for i in file.readlines()]


def checkForTLS(inp):
    for i in re.findall(r'\[(.*?)]', inp):
        if re.findall(r'(.)(?!\1)(.)\2\1', i):
            return False
    return bool(re.findall(r'(.)(?!\1)(.)\2\1', inp))


def checkForSSL(inp):
    inside = set()
    for i in re.findall(r'\[(.*?)]', inp):
        for j in re.findall(r'([a-z])(?!\1)([a-z])\1', i, overlapped=True):
            inside.add(j)
    outside = set(re.findall(r'([a-z])(?!\1)([a-z])\1', inp, overlapped=True))
    for o1, o2 in outside:
        for j1, j2 in inside:
            if (o1, o2) == (j2, j1):
                return True
    return False


print(checkForSSL('aba[aaa]bbb[bab]'))

tls = 0
ssl = 0
for i in data:
    if checkForTLS(i):
        tls += 1
    if checkForSSL(i):
        ssl += 1
print(tls)
print(ssl)
