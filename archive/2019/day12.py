# Py 3.9+
import numpy as np
from itertools import combinations
from typing import Tuple, Any
import re
from math import lcm


class Moon:
    def __init__(self, pos: Tuple[int]):
        self.pos = np.array(pos, int)
        self.vel = np.zeros((3,), int)
    
    def __repr__(self):
        return f'Moon(pos=<{self.pos}> vel=<{self.vel}>)'
    
    def __int__(self):
        return int(sum(abs(self.pos))) * int(sum(abs(self.vel)))
    
    def apply_force(self, force: np.ndarray) -> None:
        self.vel += force
    
    def step(self) -> None:
        self.pos += self.vel


#
#  Part 1
#
def simulate_gravity(moon1: Moon, moon2: Moon, index: int = None) -> None:
    """Simulates gravity and applies forces between 2 moons on either 1 or all 3 axis"""
    if index is not None:  # Only simulate 1 axis
        p1, p2 = moon1.pos[index], moon2.pos[index]
        if p1 == p2:
            return
        moon1.vel[index] += (p := 1 if p1 < p2 else -1)
        moon2.vel[index] -= p
        return
    
    # Simulate all 3 axis
    force = np.zeros((3,), int)
    for i, (p1, p2) in enumerate(zip(moon1.pos, moon2.pos)):
        if p1 < p2:
            force[i] = 1
        elif p1 > p2:
            force[i] = -1
        else:
            force[i] = 0
    
    moon1.apply_force(force)
    moon2.apply_force(-force)


def step(index: int = None) -> None:
    """Steps/ticks all moons once on either 1 or all 3 axis"""
    for i in combinations(moons, 2):
        simulate_gravity(*i, index=index)
    for moon in moons:
        moon.step()


#
#  Part 2
#
def get_axis_state(index: int) -> Tuple[Tuple[Any, Any]]:
    """Returns the state of all 4 moons on an axis in a way that can be compared"""
    return tuple((i.pos[index], i.vel[index]) for i in moons)


def cycle_on_axis(index: int) -> int:
    """Returns the number of steps required for an axis to return to its original state"""
    start_state = get_axis_state(index)
    
    step(index)
    step_count = 1
    
    while get_axis_state(index) != start_state:
        step(index)
        step_count += 1
    
    return step_count


#
#  End
#
with open('day12.txt') as file:
    data = []
    for line in file:
        data.append(tuple(map(int, re.findall(r'-?\d+', line))))

moons = list(map(Moon, data))
for _ in range(1000):
    step()
part1 = sum(map(int, moons))

moons = list(map(Moon, data))
part2 = lcm(*(cycle_on_axis(i) for i in range(3)))

print(f'Part 1: {part1}\nPart 2: {part2}')
