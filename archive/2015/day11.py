inp = [ord(i) for i in 'vzbxkghb']

def increment_password(index=len(inp)-1):
    inp[index] += 1
    if chr(inp[index]) in 'iol':
        inp[index] += 1
    if inp[index] == ord('{'):
        inp[index] = ord('a')
        increment_password(index-1)

def password_string(password=inp):
    return ''.join(map(chr, password))


def validate_password(password=inp):
    same = 0
    for i in range(len(password)-1):
        if password[i] == same:
            continue
        if password[i] == password[i+1]:
            if same:
                break
            else:
                same = password[i]
    else:
        return False
    for i in range(len(password)-2):
        if password[i] == password[i+1] - 1 == password[i+2] - 2:
            return True
    return False

while True:
    increment_password()
    if validate_password():
        break
print(password_string())

while True:
    increment_password()
    if validate_password():
        break
print(password_string())
