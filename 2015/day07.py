import numpy as np  # just for uint16
import operator


_OPERATIONS = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift
}


def _parse_expression(inp: str):
    match inp.split():
        case x,:
            if x.isdigit():
                return np.uint16(x)
            return (lambda x:x), [x]
        case 'NOT', x:
            return operator.invert, [x]
        case a, op, b:
            # convert preset values
            if a.isdigit(): a = np.uint16(a)
            if b.isdigit(): b = np.uint16(b)
            return _OPERATIONS[op], [a, b]


def _resolve_wire(circuit, target):
    if isinstance(target, np.integer):  # recursion base case
        return target
    elif isinstance(circuit[target], np.integer):  # already resolved
        return circuit[target]
    op, inputs = circuit[target]
    result = op(*(_resolve_wire(circuit, i) for i in inputs))
    circuit[target] = result  # save result for future use
    return result


def day7(data):
    # Parse input
    circuit = {}
    for row in data.splitlines():
        inputs, _, wire = row.partition(' -> ')
        circuit[wire] = _parse_expression(inputs)
    # Part 1
    circuit1 = circuit.copy()
    part1 = _resolve_wire(circuit1, 'a')
    # Part 2
    circuit2 = circuit.copy()
    circuit2['b'] = part1
    part2 = _resolve_wire(circuit2, 'a')

    return part1, part2


if __name__ == '__main__':
    with open('inputs/day07.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day7(data)))
