import pygame
from pygame.locals import *
import numpy as np
from time import time

currentFrame = 0
autoplay = False
autoFrame = time()
frameDelay = 0.05
with open('day11_output.txt') as file:
    data = [np.array([list(i) for i in line.split()], int) for line in file.read().split('\n')][:-1]

pygame.init()
SCREEN = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Day 11 visualisation')

colors = [(255, 255, 255)]+[(0, 0, i) for i in range(28, 255, 28)]
surfaces = []
for color in colors:
    s = pygame.Surface((50, 50))
    s.fill(color)
    surfaces.append(s)


r = True
while True:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == QUIT:
            exit(0)
        
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                if currentFrame > 0:
                    currentFrame -= 1
                r = True
            elif event.key == K_RIGHT:
                if currentFrame < len(data) - 1:
                    currentFrame += 1
                r = True
            elif event.key == K_UP:
                currentFrame = 0
                r = True
            elif event.key == K_DOWN:
                currentFrame = len(data) - 1
                r = True
            elif event.key == K_SPACE:
                autoplay = not autoplay
                if autoplay and currentFrame == len(data) - 1:
                    currentFrame = -1
        
    if autoplay and (t := time()) > autoFrame + frameDelay:
        autoFrame = t + frameDelay
        if currentFrame < len(data) - 1:
            currentFrame += 1
            r = True
        else:
            autoplay = False
    
    if r:
        displayGrid = data[currentFrame]
        r = False
    
    for i, x in enumerate(range(0, 500, 50)):
        for j, y in enumerate(range(0, 500, 50)):
            s = surfaces[displayGrid[i, j]]
            SCREEN.blit(s, (x, y))
    
    pygame.display.flip()
