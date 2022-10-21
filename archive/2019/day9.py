# noinspection PyShadowingNames
class IntcodeComputer:
    def __init__(self, programCode, iD=0, relBase=0, indx=0, emptySpace=1000, inptArr=None):
        self.relBase = relBase
        if inptArr is None:
            inptArr = []
        self.relativeBase = 0
        self.memory = []
        self.memory = programCode.copy()
        # noinspection PyShadowingNames
        for i in range(emptySpace):
            self.memory.append(0)
        self.index = indx
        self.inputArray = inptArr.copy()
        self.outputArray = []
        self.id = iD
        self.finished = False
    
    def compute(self):  # computes until there's an input requiered
        
        while True:
            
            if self.index == 308:
                print(self.memory[311])
            # formatting OPCODE
            
            TempLen = len(str(self.memory[self.index]))
            StringToAdd = ""
            for i in range(5 - TempLen):
                StringToAdd += "0"
            self.memory[self.index] = StringToAdd + str(self.memory[self.index])
            # print(self.memory[self.index])
            
            # reading parameters according to the given parameter modes ----------------------
            parameters = []
            parameterMode = str(self.memory[self.index][:3])
            # print(self.memory[self.index], parameterMode)
            # print(parameterMode)
            OpCode = str(self.memory[self.index])[-2:]
            self.memory[self.index] = int(self.memory[self.index])
            if parameterMode[2] == "0":
                parameters.append(int(self.memory[self.index + 1]))
            elif parameterMode[2] == "1":
                parameters.append(self.index + 1)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 1]) + self.relativeBase)
            
            if parameterMode[1] == "0":
                parameters.append(int(self.memory[self.index + 2]))
            elif parameterMode[1] == "1":
                parameters.append(self.index + 2)
            else:  # paramMode 2
                parameters.append(self.memory[self.index + 2] + self.relativeBase)
            
            if parameterMode[0] == "0":
                parameters.append(int(self.memory[self.index + 3]))
            elif parameterMode[0] == "1":
                parameters.append(self.index + 3)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 3]) + self.relativeBase)
            # param read end -----------------------------------------
            # strr=""
            # for i in range(4):
            #    strr += str(self.memory[self.index + i ] ) +"/"
            # print(self.index,strr,OpCode)
            # strr2 =""
            # for i in range(3):
            # strr2 += str(self.memory[parameters[i]] ) +"/"
            # print(strr2)
            # print("opcode:" + str(OpCode) + "  parameters: " + str(self.memory[parameters[0]]) +"/"+ str(
            # self.memory[parameters[1]]) +"/"+ str(self.memory[parameters[2]]))
            
            # reacting according to the OP CODE-----------------------------------------
            if OpCode == "01":
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) + int(self.memory[parameters[1]])
                self.index += 4
            elif OpCode == "02":
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) * int(self.memory[parameters[1]])
                self.index += 4
            elif OpCode == "03":
                if len(self.inputArray) != 0:
                    self.memory[parameters[0]] = self.inputArray[0]
                    self.index += 2
                    self.inputArray.pop(0)
                else:
                    print("waiting input")
                    break
            elif OpCode == "04":
                print("output from int comp " + str(self.id) + "  :" + str(self.memory[parameters[0]]))
                self.outputArray.append(self.memory[parameters[0]])
                self.index += 2
            elif OpCode == "05":
                if self.memory[parameters[0]] != 0:
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif OpCode == "06":
                # print("went here")
                if self.memory[parameters[0]] == 0:
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif OpCode == "07":
                if int(self.memory[parameters[0]]) < int(self.memory[parameters[1]]):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif OpCode == "08":
                if self.memory[parameters[0]] == self.memory[parameters[1]]:
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif OpCode == "09":
                self.relativeBase += self.memory[parameters[0]]
                self.index += 2
                # print("relative base has been changed")
            elif OpCode == "99":
                print(str(self.id) + ". computer has finished")
                self.finished = True
                break
            
            # print(self.relativeBase)


if __name__ == '__main__':
    data = [1102, 34463338, 34463338, 63, 1007, 63, 34463338, 63, 1005, 63, 53, 1101, 0, 3, 1000, 109, 988, 209, 12, 9,
            1000, 209, 6, 209, 3, 203, 0, 1008, 1000, 1, 63, 1005, 63, 65, 1008, 1000, 2, 63, 1005, 63, 904, 1008, 1000, 0,
            63, 1005, 63, 58, 4, 25, 104, 0, 99, 4, 0, 104, 0, 99, 4, 17, 104, 0, 99, 0, 0, 1101, 0, 252, 1023, 1101, 0, 0,
            1020, 1102, 1, 39, 1013, 1102, 1, 234, 1029, 1102, 26, 1, 1016, 1101, 37, 0, 1005, 1101, 0, 27, 1011, 1101, 21,
            0, 1000, 1101, 0, 29, 1019, 1101, 35, 0, 1003, 1102, 22, 1, 1007, 1102, 1, 32, 1001, 1101, 1, 0, 1021, 1102, 1,
            216, 1027, 1102, 30, 1, 1012, 1102, 1, 24, 1009, 1101, 36, 0, 1002, 1101, 0, 31, 1010, 1101, 0, 243, 1028, 1102,
            787, 1, 1024, 1102, 255, 1, 1022, 1102, 33, 1, 1017, 1102, 1, 23, 1004, 1102, 778, 1, 1025, 1102, 1, 28, 1008,
            1101, 0, 223, 1026, 1102, 1, 25, 1015, 1101, 0, 20, 1006, 1102, 34, 1, 1014, 1101, 38, 0, 1018, 109, -4, 1202,
            5, 1, 63, 1008, 63, 32, 63, 1005, 63, 203, 4, 187, 1106, 0, 207, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 37,
            2106, 0, -6, 1001, 64, 1, 64, 1106, 0, 225, 4, 213, 1002, 64, 2, 64, 109, 3, 2106, 0, -8, 4, 231, 1001, 64, 1,
            64, 1105, 1, 243, 1002, 64, 2, 64, 109, -12, 2105, 1, -1, 1105, 1, 261, 4, 249, 1001, 64, 1, 64, 1002, 64, 2,
            64, 109, -13, 2102, 1, -3, 63, 1008, 63, 31, 63, 1005, 63, 285, 1001, 64, 1, 64, 1106, 0, 287, 4, 267, 1002, 64,
            2, 64, 109, 6, 21102, 40, 1, 0, 1008, 1017, 40, 63, 1005, 63, 313, 4, 293, 1001, 64, 1, 64, 1105, 1, 313, 1002,
            64, 2, 64, 109, -10, 2107, 31, -6, 63, 1005, 63, 331, 4, 319, 1105, 1, 335, 1001, 64, 1, 64, 1002, 64, 2, 64,
            109, -6, 2102, 1, 7, 63, 1008, 63, 28, 63, 1005, 63, 357, 4, 341, 1105, 1, 361, 1001, 64, 1, 64, 1002, 64, 2,
            64, 109, 2, 21107, 41, 40, 8, 1005, 1011, 377, 1106, 0, 383, 4, 367, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, -1,
            1201, 2, 0, 63, 1008, 63, 26, 63, 1005, 63, 403, 1106, 0, 409, 4, 389, 1001, 64, 1, 64, 1002, 64, 2, 64, 109,
            22, 1205, -4, 425, 1001, 64, 1, 64, 1105, 1, 427, 4, 415, 1002, 64, 2, 64, 109, -9, 21101, 42, 0, 3, 1008, 1018,
            39, 63, 1005, 63, 451, 1001, 64, 1, 64, 1105, 1, 453, 4, 433, 1002, 64, 2, 64, 109, 3, 21107, 43, 44, 0, 1005,
            1018, 475, 4, 459, 1001, 64, 1, 64, 1105, 1, 475, 1002, 64, 2, 64, 109, -7, 21101, 44, 0, 0, 1008, 1011, 44, 63,
            1005, 63, 497, 4, 481, 1105, 1, 501, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 17, 1206, -7, 513, 1105, 1, 519, 4,
            507, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, -24, 1207, 5, 25, 63, 1005, 63, 537, 4, 525, 1105, 1, 541, 1001, 64,
            1, 64, 1002, 64, 2, 64, 109, 7, 21108, 45, 43, 2, 1005, 1013, 557, 1106, 0, 563, 4, 547, 1001, 64, 1, 64, 1002,
            64, 2, 64, 109, -5, 1207, -3, 34, 63, 1005, 63, 583, 1001, 64, 1, 64, 1106, 0, 585, 4, 569, 1002, 64, 2, 64,
            109, 5, 21108, 46, 46, 5, 1005, 1016, 607, 4, 591, 1001, 64, 1, 64, 1105, 1, 607, 1002, 64, 2, 64, 109, -12,
            2108, 20, 8, 63, 1005, 63, 627, 1001, 64, 1, 64, 1105, 1, 629, 4, 613, 1002, 64, 2, 64, 109, 24, 1206, -3, 647,
            4, 635, 1001, 64, 1, 64, 1105, 1, 647, 1002, 64, 2, 64, 109, -30, 2108, 32, 8, 63, 1005, 63, 665, 4, 653, 1106,
            0, 669, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 22, 1208, -9, 20, 63, 1005, 63, 691, 4, 675, 1001, 64, 1, 64,
            1106, 0, 691, 1002, 64, 2, 64, 109, -4, 21102, 47, 1, 3, 1008, 1014, 49, 63, 1005, 63, 715, 1001, 64, 1, 64,
            1105, 1, 717, 4, 697, 1002, 64, 2, 64, 109, -10, 2101, 0, 1, 63, 1008, 63, 36, 63, 1005, 63, 743, 4, 723, 1001,
            64, 1, 64, 1105, 1, 743, 1002, 64, 2, 64, 109, 16, 1201, -9, 0, 63, 1008, 63, 28, 63, 1005, 63, 769, 4, 749,
            1001, 64, 1, 64, 1105, 1, 769, 1002, 64, 2, 64, 109, 2, 2105, 1, 5, 4, 775, 1001, 64, 1, 64, 1106, 0, 787, 1002,
            64, 2, 64, 109, -5, 1202, -6, 1, 63, 1008, 63, 26, 63, 1005, 63, 807, 1106, 0, 813, 4, 793, 1001, 64, 1, 64,
            1002, 64, 2, 64, 109, -16, 2107, 37, 4, 63, 1005, 63, 833, 1001, 64, 1, 64, 1105, 1, 835, 4, 819, 1002, 64, 2,
            64, 109, 2, 2101, 0, 1, 63, 1008, 63, 34, 63, 1005, 63, 855, 1105, 1, 861, 4, 841, 1001, 64, 1, 64, 1002, 64, 2,
            64, 109, 19, 1205, 2, 875, 4, 867, 1105, 1, 879, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, -2, 1208, -8, 23, 63,
            1005, 63, 899, 1001, 64, 1, 64, 1106, 0, 901, 4, 885, 4, 64, 99, 21101, 0, 27, 1, 21102, 915, 1, 0, 1106, 0,
            922, 21201, 1, 61455, 1, 204, 1, 99, 109, 3, 1207, -2, 3, 63, 1005, 63, 964, 21201, -2, -1, 1, 21102, 942, 1, 0,
            1105, 1, 922, 22102, 1, 1, -1, 21201, -2, -3, 1, 21102, 1, 957, 0, 1105, 1, 922, 22201, 1, -1, -2, 1106, 0, 968,
            22101, 0, -2, -2, 109, -3, 2105, 1, 0]
    
    comp1 = IntcodeComputer(data, inptArr=[1])
    comp1.compute()
    
    comp2 = IntcodeComputer(data, inptArr=[2])
    comp2.compute()
