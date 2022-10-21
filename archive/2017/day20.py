import re
import numpy as np
from time import time


class Particle:
    pID = 0

    def __init__(self, pos, vel, acc):
        self.position = pos
        self.velocity = vel
        self.acceleration = acc
        self.id = Particle.pID
        Particle.pID += 1

    def runFrame(self):
        self.velocity += self.acceleration
        self.position += self.velocity

    def distance(self):
        return sum(map(abs, self.position))


def parseData(string):
    return Particle(*[np.array(eval(i)) for i in re.findall(r'<(.*?)>', string.strip())])


with open('day20.txt') as file:
    particles = [parseData(i) for i in file.readlines()]

lastTime = time()
for _ in range(3000):
    removeCandidates = set()
    for i in range(len(particles)):
        particles[i].runFrame()
        for j in range(i):
            if str(particles[i].position) == str(particles[j].position):
                removeCandidates = removeCandidates.union({i, j})
    for i in reversed(sorted(removeCandidates)):
        particles.pop(i)
    print(f'frame {_+1} - {len(removeCandidates)}c / {len(particles)} / {time()-lastTime:.2f}s')
    lastTime = time()
print(len(particles))
