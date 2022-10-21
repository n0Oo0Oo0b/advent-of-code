from time import sleep

with open('day25_output.txt') as file:
    data = file.read().split('\n\n\n\n')

for i in data:
    print(('\n' * 20) + i)
    sleep(0.2)
