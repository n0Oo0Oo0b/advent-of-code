from numpy import uint16

with open('day7.txt') as file:
    raw = [i.strip().split(' -> ') for i in file.readlines()]

data = {out:inp for inp, out in raw}

def get_value(key):
    if key.isdecimal():
        return uint16(key)
    if isinstance(data[key], uint16):
        return data[key]
    match data[key].split():
        case a, 'AND', b:
            val = get_value(a) & get_value(b)
        case a, 'OR', b:
            val = get_value(a) | get_value(b)
        case a, 'LSHIFT', b:
            val = get_value(a) << get_value(b)
        case a, 'RSHIFT', b:
            val = get_value(a) >> get_value(b)
        case 'NOT', a:
            val = ~ get_value(a)
        case a, :
            val = get_value(a)
    data[key] = val
    return val

a = get_value('a')
print(a)

data = {out:inp for inp, out in raw}
data['b'] = uint16(a)

print(get_value('a'))
