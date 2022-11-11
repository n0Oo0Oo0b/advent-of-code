import operator

TARGET_PROPERTIES = {
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

def parse_properties(inp):
    output = {}
    for i in inp.split(', '):
        name, _, value = i.partition(': ')
        output[name] = int(value)
    return output


def day16(inp):
    part1, part2 = None, None
    for row in inp.splitlines():
        # Parse line
        sue, _, raw_properties = row.partition(': ')
        properties = parse_properties(raw_properties)
        # Part 1
        if properties.items() <= TARGET_PROPERTIES.items():  # checks for subsets of TARGET_PROPERTIES
            part1 = int(sue.split()[1])
        # Part 2
        for property, value in properties.items():
            if property not in TARGET_PROPERTIES:  # skip because nonexistent
                continue
            # Identify search type (>, <, ==)
            if property in ('cats', 'trees'): op = operator.gt
            elif property in ('pomeranians', 'goldfish'): op = operator.lt
            else: op = operator.eq
            # Match property
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
