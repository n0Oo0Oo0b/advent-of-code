with open('day18.txt') as file:
    data = [i.strip().split(' ') for i in file.readlines()]


class ExitException(Exception):
    pass


class Program:
    def __init__(self, programID, programs):
        self.registers = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.registers[char] = 0
        self.registers['p'] = int(programID)
        self.data = programs
        self.receiveQueue = []
        self.index = 0
        self.id = programID

    def getValue(self, value):
        try:
            return int(value)
        except ValueError:
            return self.registers[value]

    def runStep(self):
        cmd = self.data[self.index]
        if cmd[0] == 'snd':
            self.index += 1
            return self.getValue(cmd[1])
        elif cmd[0] == 'set':
            self.registers[cmd[1]] = self.getValue(cmd[2])
        elif cmd[0] == 'add':
            self.registers[cmd[1]] += self.getValue(cmd[2])
        elif cmd[0] == 'mul':
            self.registers[cmd[1]] *= self.getValue(cmd[2])
        elif cmd[0] == 'mod':
            self.registers[cmd[1]] %= self.getValue(cmd[2])
        elif cmd[0] == 'rcv':
            if self.receiveQueue:
                self.registers[cmd[1]] = self.receiveQueue.pop(0)
            else:
                return 'wait'
        elif cmd[0] == 'jgz':
            if self.getValue(cmd[1]) > 0:
                self.index += self.getValue(cmd[2]) - 1
        self.index += 1
        if self.index > len(self.data):
            raise ExitException


programs = [Program(0, data), Program(1, data)]
a = 0
prevA = -1
while prevA != a:
    prevA = a
    rV = ''
    while rV != 'wait':
        rV = programs[0].runStep()
        if (rV is not None) and (rV != 'wait'):
            programs[1].receiveQueue.append(rV)
    rV = ''
    while rV != 'wait':
        rV = programs[1].runStep()
        if (rV is not None) and (rV != 'wait'):
            programs[0].receiveQueue.append(rV)
            a += 1
            break
print(a)
