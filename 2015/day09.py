from itertools import permutations


def day09(data):
    # Parse input
    nodes = set()
    distances = {}
    for row in data.splitlines():
        path_nodes, _, distance = row.partition(' = ')
        path_nodes = frozenset(path_nodes.split(' to '))
        nodes |= path_nodes
        distances[path_nodes] = int(distance)
    # Solve (brute force)
    min_ = float('inf')
    max_ = 0
    for path in permutations(nodes):
        path_distance = sum(distances[frozenset(path[i:i+2])] for i in range(len(path)-1))
        min_ = min(min_, path_distance)
        max_ = max(max_, path_distance)
    return min_, max_


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day09(data)))
