from dataclasses import dataclass

from util import *

res = 0


@dataclass
class Lens:
    label: str
    focus: int

    def __eq__(self, other):
        return self.label == other.label


def hash_(s):
    s = list(map(ord, s))
    v = 0
    for c in s:
        v += c
        v *= 17
        v %= 256
    return v


boxes = [[] for _ in range(256)]
for i in data:
    if '-' in i:
        label = i[:-1]
        try:
            boxes[hash_(label)].remove(Lens(label, -1))
        except ValueError:
            pass
    else:
        label, b = i.split("=")
        box = boxes[hash_(label)]
        if Lens(label, -1) in box:
            box[box.index(Lens(label, -1))] = Lens(label, int(b))
        else:
            box.append(Lens(label, int(b)))

for p, box in enumerate(boxes, 1):
    for l, x in enumerate(box, 1):
        res += p * l * x.focus
