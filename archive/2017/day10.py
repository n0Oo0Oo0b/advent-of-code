def fullHash(inp):
    dx = [ord(i) for i in inp] + [17, 31, 73, 47, 23]
    
    l = [i for i in range(256)]
    
    s = 0
    i = 0
    
    for k in range(64):
        for d in dx:
            j = i + d
            
            l = l * 3
            l = (l[:i] + l[i:j][::-1] + l[j:])[256:]
            l = (l[:i] + l[i:j][::-1] + l[j:])[:256]
            
            i = (i + d + s) % 256
            s += 1
    
    h = ''
    
    for i in range(16):
        d = 0
        
        for j in l[i * 16:(i + 1) * 16]:
            d = d ^ j
        
        h += '{:0>2}'.format(hex(d)[2:])
    
    return h


if __name__ == '__main__':
    print(fullHash('183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'))
