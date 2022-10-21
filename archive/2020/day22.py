data = '''Player 1:
48
23
9
34
37
36
40
26
49
7
12
20
6
45
14
42
18
31
39
47
44
15
43
10
35

Player 2:
13
19
21
32
27
16
11
29
41
46
33
1
30
22
38
5
17
4
50
2
3
28
8
25
24'''.split('\n')

ex1 = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''.split('\n')

# data = ex1

player1 = [ int(i) for i in data[1:data.index('')] ]
player2 = [ int(j) for j in data[data.index('')+2:] ]
def play(player1,player2):
    while player1 and player2:
        p1c = player1.pop(0)
        p2c = player2.pop(0)
        if p1c > p2c:
            player1.append(p1c)
            player1.append(p2c)
        else:
            player2.append(p2c)
            player2.append(p1c)

    if player1:
        winner = player1
    else:
        winner = player2
    return winner

winner = play(player1,player2)
winner.reverse()
score = 0
for i,j in enumerate(winner):
    score += (i+1)*j
print(score)
