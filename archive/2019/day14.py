from collections import defaultdict

with open('day14.txt') as file:
    data = {}
    for line in file:
        line = line.strip()
        raw_reactants, raw_result = line.split(' => ')
        reactants = []
        for i in raw_reactants.split(', '):
            count, chemical = i.split()
            reactants.append((int(count), chemical))
        
        count, chemical = raw_result.split()
        
        data[chemical] = (int(count), reactants)


extra_items = defaultdict(int)


def ore_required(name, quantity=1):
    if extra_items[name] > quantity:
        extra_items[name] -= quantity
        return 0

    count_per_reaction, reactants = data[name]
    
    quantity -= extra_items[name]
    extra_items[name] = quantity % count_per_reaction
    
    reaction_count = -(-quantity//count_per_reaction)
    
    total_ore = 0
    for count, reactant in reactants:
        if reactant == 'ORE':
            total_ore += count
        else:
            total_ore += ore_required(reactant, count)
    
    return total_ore * reaction_count


print(ore_required('FUEL'))
