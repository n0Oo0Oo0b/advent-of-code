raw = open(0).read().splitlines()

width = len(raw[0])-2
height = len(raw)-2
directions = {
    '<': -1+0j,
    '>': 1+0j,
    '^': -1j,
    'v': 1j
}


def wrap(location):
    return complex((location.real-1) % width + 1, (location.imag-1) % height + 1)


blizzards = set()
border = {1-1j}
for y, line in enumerate(raw):
    for x, char in enumerate(line):
        if char == '.':
            continue
        elif char == '#':
            border.add(x+y*1j)
        else:
            blizzards.add((x+y*1j, directions[char]))
target = x-1 + y*1j
start = 1+0j
border.add(target+1j)


def tick_blizzard():
    global blizzards
    new_blizzards = set()
    blizzard_locations = set()
    for location, direction in blizzards:
        new_location = wrap(location + direction)
        blizzard_locations.add(new_location)
        new_blizzards.add((new_location, direction))
    blizzards = new_blizzards
    return blizzard_locations


n = 0
states = {start}
while target not in states:
    blizzard_locations = tick_blizzard()
    new_states = set()
    for location in states:
        possible_next = {location, location+1, location-1, location+1j, location-1j}
        possible_next -= blizzard_locations | border
        new_states |= possible_next
    n += 1
    states = new_states
print(n)
states = {target}
while start not in states:
    blizzard_locations = tick_blizzard()
    new_states = set()
    for location in states:
        possible_next = {location, location+1, location-1, location+1j, location-1j}
        possible_next -= blizzard_locations | border
        new_states |= possible_next
    n += 1
    states = new_states
states = {start}
while target not in states:
    blizzard_locations = tick_blizzard()
    new_states = set()
    for location in states:
        possible_next = {location, location+1, location-1, location+1j, location-1j}
        possible_next -= blizzard_locations | border
        new_states |= possible_next
    n += 1
    states = new_states
print(n)
