import json

def total_json(inp, ignore_red=False):
    if isinstance(inp, int):
        return inp
    elif isinstance(inp, str):
        return 0
    elif isinstance(inp, dict):
        inp = inp.values()
        if ignore_red and 'red' in inp:
            return 0
    return sum(total_json(i, ignore_red) for i in inp)

def day12(data):
    d = json.loads(data)
    return total_json(d), total_json(d, True)

if __name__ == '__main__':
    with open('inputs/day12.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day12(data)))
