import re

INPUT = '1113122113'


def runCycle(inp):
    return ''.join([str(len(j)) + i for i, j in re.findall(r'(?=(\d))(\1+)', inp)])


for _ in range(50):
    INPUT = runCycle(INPUT)
print(len(INPUT))
