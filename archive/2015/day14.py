import re
import numpy as np


class Reindeer:
    def __init__(self, speed, stamina, cooldown) -> None:
        self.speed = speed
        self.stamina = stamina
        self.cooldown = cooldown
        self.cycle_distance = speed * stamina
        self.cycle_time = stamina + cooldown

    def distance_at_time(self, time):
        cycle_count, remainder = divmod(time, self.cycle_time)
        travelled = cycle_count * self.cycle_distance
        travelled += self.speed * min(remainder, self.stamina)
        return travelled

    def distances_until_time(self, time):
        distances = [0]
        while len(distances) - 1 < time:
            next_value = distances[-1] + self.speed
            distances.extend(range(next_value, next_value + self.cycle_distance, self.speed))
            distances += [distances[-1]] * self.cooldown
        return distances[1:time+1]

with open('day14.txt') as file:
    data = [re.findall(r'\d+', i) for i in file.read().split('\n')]

reindeer = [Reindeer(*map(int,i)) for i in data]

furthest = 0
for i in reindeer:
    furthest = max(furthest, i.distance_at_time(2503))
print(furthest)

live_distances = np.array([i.distances_until_time(2503) for i in reindeer])
print((live_distances == live_distances.max(0)).sum(1).max())
