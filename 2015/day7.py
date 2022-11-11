from numpy import uint16
import operator

OPERATIONS = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift
}

def parse_expression(inp: str) -> tuple[callable, list[str|uint16]] | uint16:
    match inp.split():
        case x,:
            if x.isdigit():
                return uint16(x)
            return (lambda x:x), [x]
        case 'NOT', x:
            return operator.invert, [x]
        case a, op, b:
            # convert preset values
            if a.isdigit(): a = uint16(a)
            if b.isdigit(): b = uint16(b)
            return OPERATIONS[op], [a, b]

def resolve_item(circuit, inp):
    if isinstance(inp, uint16): return inp
    else: return resolve_wire(circuit, inp)  # recurse

def resolve_wire(circuit, target='a'):
    if isinstance(circuit[target], uint16):  # already resolved
        return circuit[target]

    op, inputs = circuit[target]
    result = op(*(resolve_item(circuit, i) for i in inputs))
    circuit[target] = result  # save result for future use
    return result

def day7(data):
    circuit = {}
    for row in data.splitlines():
        inputs, _, wire = row.partition(' -> ')
        circuit[wire] = parse_expression(inputs)

    # Part 1
    circuit1 = circuit.copy()
    part1 = resolve_wire(circuit1)

    # Part 2
    circuit2 = circuit.copy()
    circuit2['b'] = part1
    part2 = resolve_wire(circuit2)

    return part1, part2


if __name__ == '__main__':
    with open('inputs/day7.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day7(data)))
