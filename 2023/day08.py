from itertools import *
from util import *


res = 0

graph = {}

instructions, graph_data = data.split("\n\n")

for line in graph_data.split("\n"):
    a, b, c = re.match(r"(.{3}) = \((.{3}), (.{3})\)", line).groups()
    graph[a] = b, c


def it_states(current):
    for i, direction in cycle(enumerate(instructions)):
        current = graph[current][direction == 'R']
        yield i, current


cycles = []
for c in [i for i in graph if i[-1] == "A"]:
    path = [(0, c)]
    seen = {(0, c)}
    for i in it_states(c):
        if i in seen:
            cycles.append((path.index(i), path))
            break
        seen.add(i)
        path.append(i)
    print(c, len(path), i)


# with open("temp.txt", 'w') as f:
#     f.write(str(sizes))

# with open("temp.txt") as f:
#     data = eval(f.read())
#
# x = sp.Symbol("x")
#
# e = []
# for r_start, path in data:
#     a = 0
#     size = len(path)
#     for i, (_, loc) in enumerate(path):
#         if loc[-1] == 'Z':
#             a = i
#             break
#     print(i, size, r_start)
#     print(a / 283)
#     e.append(a)
# res = lcm(*e)
# # res = sp.solve(e, x)
