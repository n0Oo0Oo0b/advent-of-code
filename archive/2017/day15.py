class Generator:
    def __init__(self, startingNum, multNum, divCondition):
        self.prevNum = startingNum
        self.multNum = multNum
        self.divNum = divCondition
    
    def getNextValue(self):
        num = -1
        while num % self.divNum != 0:
            num = (self.prevNum * self.multNum) % 2147483647
            self.prevNum = num
        return bin(num)[-16:]


genA = Generator(634, 16807, 4)
genB = Generator(301, 48271, 8)
t = 0
for i in range(5000000):
    if genA.getNextValue() == genB.getNextValue():
        t += 1
    if i % 500000 == 0:
        print(i)
print(t)
