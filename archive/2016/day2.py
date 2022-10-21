with open('day2.txt') as file:
    data = file.read().split('\n')


def getKey():
    match cX, cY:
        case 0, -2: return '1'
        case d, -1: return str(d+3)
        case d, 0: return str(d+7)
        case d, 1: return ('A', 'B', 'C')[d+1]
        case _, _: return 'D'


cX = -2
cY = 0
passcode = ''
for pattern in data:
    for direction in pattern:
        match direction:
            case 'U':
                if getKey() not in '52149':
                    cY -= 1
            case 'D':
                if getKey() not in '5ADC9':
                    cY += 1
            case 'L':
                if getKey() not in '125AD':
                    cX -= 1
            case 'R':
                if getKey() not in '149CD':
                    cX += 1
    passcode += getKey()

print(passcode)
