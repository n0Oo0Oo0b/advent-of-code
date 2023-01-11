import re
import operator
from aocd import lines

data = {}
for line in lines:
    a, b = line.split(': ')
    data[a] = b


def resolve(d, name='root'):
    target = d[name]
    if isinstance(target, complex):
        return target
    elif target.isdigit():
        d[name] = int(d[name])
        return d[name]
    else:
        a, op, b = target.split()
        a = resolve(d, a)
        b = resolve(d, b)
        d[name] = {'*': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub}[op](a, b)
        return d[name]


print(resolve(data.copy()))
a, _, b = data['root'].split()
data['humn'] = 1j
result = resolve(data, a) - resolve(data, b)
print(abs(round(result.real / result.imag)))
