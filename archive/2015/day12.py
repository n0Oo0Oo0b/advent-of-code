import re
import json

with open('day12.json') as file:
    data = file.read()

print(sum(int(i) for i in re.findall(r'-?\d+', data)))


with open('day12.json') as file:
    data = json.load(file)

def total(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    
    if isinstance(obj, dict):
        obj = obj.values()
        if 'red' in obj:
            return 0
    return sum(map(total, obj))

print(total(data))
