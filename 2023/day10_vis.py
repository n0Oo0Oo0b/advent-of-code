from enum import Enum
from itertools import product

import pygame
import pygame.gfxdraw
from pygame import Vector2


with open("input.txt") as file:
    puzzle_input = file.read()


class Dir(Enum):
    NORTH = Vector2(0, -1)
    EAST = Vector2(1, 0)
    SOUTH = Vector2(0, 1)
    WEST = Vector2(-1, 0)

    def rot_cw(self):
        return Dir(self.value.rotate(90))

    def rot_ccw(self):
        return Dir(self.value.rotate(-90))


class Grid:
    start_color = (0, 255, 0)
    pipe_color = (255, 255, 255)
    loop_color = (255, 255, 0)
    connected_color = (255, 128, 128)
    inside_color = (0, 255, 0)
    symbol_mappings = {
        "|": {Dir.NORTH, Dir.SOUTH},
        "-": {Dir.EAST, Dir.WEST},
        "F": {Dir.EAST, Dir.SOUTH},
        "7": {Dir.WEST, Dir.SOUTH},
        "L": {Dir.EAST, Dir.NORTH},
        "J": {Dir.WEST, Dir.NORTH},
    }

    def __init__(self, data, start_pos):
        self.start_pos = Vector2(start_pos)
        self.data = data
        self.connected = set()
        self.loop = []
        self.loop_set = set()
        self.inside_points = set()
        self.refresh_loops()
        self.refresh_inside()

    @classmethod
    def from_puzzle_input(cls, input_):
        lines = input_.split("\n")
        data = []
        start_pos = None
        for line in lines:
            row = []
            for char in line:
                if directions := cls.symbol_mappings.get(char):
                    row.append(directions)
                elif char == "S":
                    start_pos = len(row), len(data)
                    row.append({Dir.NORTH, Dir.EAST, Dir.SOUTH, Dir.WEST})
                    # row.append({Dir.NORTH, Dir.SOUTH})
                elif char == ".":
                    row.append(set())
                else:
                    raise ValueError(f"Invalid character in input: {char}")
            data.append(row)
        if start_pos is None:
            raise ValueError("No start position found")
        return cls(data, start_pos)

    @staticmethod
    def pos_to_screen(pos, scale):
        x, y = pos
        return scale // 2 + x * scale, scale // 2 + y * scale

    @staticmethod
    def draw_cell(surf, color, center, directions, size):
        pygame.draw.circle(surf, color, center, 1)
        for direction in directions:
            pygame.draw.line(
                surf,
                color,
                center,
                center + direction.value * size,
                1,
            )

    def is_inbound(self, pos):
        x, y = pos
        return 0 <= x < len(self.data[0]) and 0 <= y < len(self.data)

    def __getitem__(self, item):
        x, y = map(int, item)
        if not self.is_inbound((x, y)):
            return set()
        return self.data[y][x]

    def __setitem__(self, key, value):
        x, y = map(int, key)
        if not self.is_inbound((x, y)):
            return
        self.data[y][x] = value

    def rotate_pos(self, pos):
        current = self[pos]
        new = {i.rot_cw() for i in current}
        self[pos] = new
        self.refresh_loops()
        self.refresh_inside()

    def flip_pos(self, pos):
        current = self[pos]
        if not current:
            self[pos] = self.symbol_mappings["|"]
        elif current in (self.symbol_mappings["|"], self.symbol_mappings["-"]):
            self[pos] = self.symbol_mappings["L"]
        else:
            self[pos] = set()
        self.refresh_loops()
        self.refresh_inside()

    def refresh_loops(self):
        self.connected.clear()
        self.loop = []
        for direction in Dir:
            current_pos = self.start_pos.copy()
            current_path = [tuple(map(int, current_pos))]
            while True:
                current_pos += direction.value
                if current_pos == self.start_pos:
                    self.loop = current_path
                    break
                new = self[current_pos]
                reverse = Dir(-direction.value)
                if reverse not in new:
                    break
                direction, = new - {reverse}
                pos = tuple(map(int, current_pos))
                current_path.append(pos)
            self.connected |= set(current_path)
        self.loop_set = set(self.loop)

    def refresh_inside(self):
        self.inside_points.clear()
        for y in range(len(self.data)):
            tp = bp = 0
            for x in range(len(self.data[0])):
                if (x, y) in self.loop_set and Dir.NORTH in self[x, y]:
                    tp += 1
                if (x, y) in self.loop_set and Dir.SOUTH in self[x, y]:
                    bp += 1
                if bp % 2 and tp % 2 and (x, y) not in self.loop_set:
                    self.inside_points.add((x, y))

    def draw(self, surf, pos, size, scale):
        yr = range(pos[0], pos[0] + size[0])
        xr = range(pos[1], pos[1] + size[1])
        for (g_yi, y), (g_xi, x) in product(enumerate(yr), enumerate(xr)):
            # if not self.is_inbound((y, x)):
            #     continue
            screen_pos = self.pos_to_screen((g_xi, g_yi), scale)
            if (x, y) in self.loop_set:
                color = self.loop_color
            elif (x, y) in self.connected and not self.loop:
                color = self.connected_color
            else:
                color = self.pipe_color
            self.draw_cell(
                surf, color, screen_pos, self[x, y], scale // 2,
            )
            if (x, y) in self.inside_points:
                pygame.draw.circle(
                    surf, self.inside_color, screen_pos, scale // 5,
                )

        if self.loop:
            pygame.gfxdraw.filled_polygon(
                surf,
                [
                    self.pos_to_screen((i - pos[1], j - pos[0]), scale)
                    for i, j in self.loop
                ],
                (255, 255, 0, 24),
            )


grid = Grid.from_puzzle_input(puzzle_input)


# Setup pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
scale = 10
offset = [0, 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))
pygame.display.set_caption("Day 10 - Pipe maze")

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos = (x // scale + offset[1], y // scale + offset[0])
            if event.button == pygame.BUTTON_LEFT:
                grid.rotate_pos(pos)
            elif event.button == pygame.BUTTON_RIGHT:
                grid.flip_pos(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset[1] -= 5
            elif event.key == pygame.K_RIGHT:
                offset[1] += 5
            elif event.key == pygame.K_DOWN:
                offset[0] += 5
            elif event.key == pygame.K_UP:
                offset[0] -= 5
            elif event.key == pygame.K_EQUALS:
                scale += 5
            elif event.key == pygame.K_MINUS:
                if scale > 5:
                    scale -= 5

    screen.blit(background, (0, 0))
    grid.draw(screen, offset, (WIDTH // scale, HEIGHT // scale), scale)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
