with open('day5.txt') as file:
    data = [int(i) for i in file.read().split(',')]


def getCmd(inp):
    inp = str(inp)
    while len(inp) < 5:
        inp = '0' + inp
    trueCmd = int(inp[3:])
    cmdModes = list(map(int, reversed(inp[:3])))
    return [trueCmd] + cmdModes


def run(opcode, inputs=None):
    if inputs is None:
        inputs = []
    outputs = []
    pointer = 0
    
    def v(value, mode):
        if mode:
            return value
        else:
            return opcode[value]
    
    while True:
        cmd = getCmd(opcode[pointer])
        m1, m2 = cmd[1], cmd[2]
        try:
            v1 = v(opcode[pointer + 1], m1)
            v2 = v(opcode[pointer + 2], m2)
        except IndexError:
            pass
        match cmd[0]:
            case 99:
                break
            case 1:
                opcode[opcode[pointer + 3]] = v1 + v2
                increment = 4
            case 2:
                opcode[opcode[pointer + 3]] = v1 * v2
                increment = 4
            case 3:
                opcode[opcode[pointer + 1]] = inputs.pop(0)
                increment = 2
            case 4:
                outputs.append(v(opcode[pointer + 1], m1))
                increment = 2
            case 5:
                if v1:
                    pointer = v2
                    increment = 0
                else:
                    increment = 3
            case 6:
                if not v1:
                    pointer = v2
                    increment = 0
                else:
                    increment = 3
            case 7:
                opcode[opcode[pointer + 3]] = int(v1 < v2)
                increment = 4
            case 8:
                opcode[opcode[pointer + 3]] = int(v1 == v2)
                increment = 4
            case _:
                raise ValueError(f'unrecognized opcode {getCmd(opcode[pointer])[0]}')
        pointer += increment
    return outputs


output = run(data.copy(), [5])[-1]
print(output)
