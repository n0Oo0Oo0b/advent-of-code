from aocd import lines as inp


class Node:
    nodes = {}

    def __init__(self, x, y, value):
        self.pos = x, y
        Node.nodes[x, y] = self
        self.value = value
        self.possible_next = set()
        self.possible_prev = set()
        self._dist = None

    @property
    def distance_to_end(self):
        return self._dist

    @distance_to_end.setter
    def distance_to_end(self, value):
        if self._dist is None:
            self._dist = value

    def update(self):
        x, y = self.pos
        for pos in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            node = Node.nodes.get(pos)
            if node and node.value >= self.value - 1:
                self.possible_prev.add(node)
            if node and node.value <= self.value + 1:
                self.possible_next.add(node)


for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == 'S':
            start = Node(i, j, ord('a'))
        elif char == 'E':
            end = Node(i, j, ord('z'))
        else:
            Node(i, j, ord(char))

nodes = list(Node.nodes.values())
for node in nodes:
    node.update()

seen = {start}
i = 0
while end not in seen:
    new = set()
    for node in seen:
        new |= node.possible_next
    seen |= new
    i += 1
part1 = i

i = 0
seen = {end}
prev_new = {end}
while not any(i.value == ord('a') for i in seen):
    new = set()
    for node in prev_new:
        node.distance_to_end = i
        new |= node.possible_prev - seen
    prev_new = new
    seen |= new
    i += 1
part2 = i

print(part1, part2)
