from itertools import cycle

with open('day15.txt') as file:
    data = list(map(int, file.read()))

BASE_PATTERN = [0, 1, 0, -1]


def get_pattern(digit):
    first = True
    for i in cycle(BASE_PATTERN):
        for _ in range(digit):
            if first:
                first = False
                continue
            yield i


def get_next_phase(signals):
    output = []
    for digit in range(1, 9):
        t = 0
        for i, multiplier in zip(range(len(signals)), get_pattern(digit)):
            t += signals[i] * multiplier
        output.append(abs(t) % 10)
    return output


n = get_pattern(2)
for _ in range(20):
    print(n.__next__())

for _ in range(100):
    data = get_next_phase(data)
print(data)
