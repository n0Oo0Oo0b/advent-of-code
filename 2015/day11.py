def increment(password, index=-1):
    if password[index] in (104, 110, 107):  # ord('h'), ord('k'), ord('n')
        password[index] += 2  # skip i, o and l
    else:
        password[index] += 1
    if password[index] == 123:  # ord('{'), increment next digit
        password[index] = 97  # ord('a')
        if index % len(password) > 0:
            increment(password, index-1)

def validate(password):
    # Kinda inefficient (2 loops instead of 1), I might improve later
    repeat = False
    for i in range(len(password) - 1):  # repeat letters
        if password[i] == password[i+1] != repeat:
            if not repeat:
                repeat = password[i]  # first pair
            else:
                break  # second pair
    else:
        return False
    for i in range(len(password) - 2):  # sequence (abc)
        if password[i] == password[i+1]-1 == password[i+2]-2:
            return True
    return False

def day11(data: str):
    password = [ord(i) for i in data]
    part1 = None
    while True:
        increment(password)
        if validate(password):
            if part1 is None:
                part1 = ''.join(chr(i) for i in password)
            else:
                break
    return part1, ''.join(chr(i) for i in password)


if __name__ == '__main__':
    with open('inputs/day11.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day11(data)))
