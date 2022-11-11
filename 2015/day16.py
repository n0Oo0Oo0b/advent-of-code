import operator


def _parse_properties(inp):
    output = {}
    for i in inp.split(', '):
        name, _, value = i.partition(': ')
        output[name] = int(value)
    return output


def day16(inp):
    TARGET_PROPERTIES = {  # fixed data
        'children': 3, 
        'cats': 7, 
        'samoyeds': 2, 
        'pomeranians': 3, 
        'akitas': 0, 
        'vizslas': 0, 
        'goldfish': 5, 
        'trees': 3, 
        'cars': 2, 
        'perfumes': 1
    }
    part1 = None
    part2 = None
    for line in inp.splitlines():
        # Parse line
        sue, _, raw_properties = line.partition(': ')
        properties = _parse_properties(raw_properties)
        # Match part 1
        if properties.items() <= TARGET_PROPERTIES.items():  # checks for subsets of TARGET_PROPERTIES
            part1 = int(sue.split()[1])
        # Match part 2
        for property, value in properties.items():
            if property not in TARGET_PROPERTIES:  # skip because you don't remember
                continue
            # Identify match type (>, <, ==)
            if property in ('cats', 'trees'): op = operator.gt
            elif property in ('pomeranians', 'goldfish'): op = operator.lt
            else: op = operator.eq
            # Check if value matches
            if not op(value, TARGET_PROPERTIES[property]):
                break
        else:  # Everything is valid
            part2 = int(sue.split()[1])

        if part1 and part2:  # Early exit
            break
    return part1, part2


if __name__ == '__main__':
    with open('inputs/day16.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day16(data)))
