data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0]

def runFunc(f,d):
    function = f[0]
    if function == 1:
        return f[3],d[f[1]]+d[f[2]]
    elif function == 2:
        return f[3],d[f[1]]*d[f[2]]
    elif function == 99:
        return None,None

def runProgram(d):
    for i in range(int(len(d)/4)):
        index,item = runFunc(d[4*i:4*(i+1)],d)
        try:
            d[index] = item
        except TypeError:
            break
    return d[0]

if __name__ == '__main__':
    # part 1
    d = data.copy()
    d[1] = 12
    d[2] = 2

    print(runProgram(d))

    # part 2
    for i in range(99):
        for j in range(99):
            d = data.copy()
            d[1] = i
            d[2] = j
            if runProgram(d) == 19690720:
                print(i*100+j)
