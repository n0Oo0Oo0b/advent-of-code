data = '''74666
50584
105124
52607
101692
137055
88127
77258
134816
139494
146549
144281
128146
148561
123728
114596
53743
81414
88075
70087
51497
95609
135773
71755
55037
134049
103570
122545
75969
79951
72989
128676
142001
80835
98099
81160
111114
128466
115687
147790
78965
121587
142632
61938
73285
55943
144393
68943
82827
73811
79762
83621
103134
106771
119852
77535
133417
81342
78363
145086
122420
149187
120571
50512
113307
100485
80463
79542
63275
120851
69695
70107
130390
135537
114589
75459
103546
127712
84294
83598
59834
125312
146371
131623
132985
79510
97024
78880
65949
140216
99447
144262
56745
104707
132649
140230
129059
135470
107519
107895'''.split('\n')

# part 1
print(sum([ (int(i)//3)-2 for i in data ]))

# part 2
def getFuelNeeded(mass):
    total = 0
    f = mass
    while f >= 0:
        f = (f//3)-2
        total += f
    return total-f
print(sum([ getFuelNeeded(int(i)) for i in data ]))
