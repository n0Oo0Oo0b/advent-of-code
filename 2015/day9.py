from itertools import permutations


def day9(data):
    nodes = set()
    distances = {}
    for row in data.splitlines():
        path_nodes, _, distance = row.partition(' = ')
        path_nodes = frozenset(path_nodes.split(' to '))
        nodes |= path_nodes
        distances[path_nodes] = int(distance)

    min_ = float('inf')
    max_ = 0
    for path in permutations(nodes):  # brute force because input isn't that big
        path_distance = sum(distances[frozenset(path[i:i+2])] for i in range(len(path)-1))
        min_ = min(min_, path_distance)
        max_ = max(max_, path_distance)

    return min_, max_


if __name__ == '__main__':
    with open('inputs/day9.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day9(data)))