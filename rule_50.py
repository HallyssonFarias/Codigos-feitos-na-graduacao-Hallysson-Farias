import numpy as np
import pygame
# import numpy as np
# from scipy import signal
# import os
# from datetime import datetime

# variáveis de tela
WIDTH, HEIGHT = 1900, 1000
CELL_SZ = 10
grid_w = WIDTH // CELL_SZ
grid_h = HEIGHT // CELL_SZ

#cores poderia ser definido no argumento mas fica com frescura e n sei pq xD
color_bg = (200,200,200)
black_color = (0,0,0)
white_color = (255,255,255)
pink = (255,192,203)

grid = np.full((grid_h,grid_w), 'white')
grid[0, grid_w // 2] = 'pink'
pink = 'pink'

def draw_rect():
    for x in range(WIDTH//CELL_SZ):
        for y in range(HEIGHT // CELL_SZ):
            color = pink if grid[y,x] == 'pink' else white_color
            pygame.draw.rect(screen, color, pygame.Rect(x* CELL_SZ + 1,y * CELL_SZ+1, CELL_SZ-2, CELL_SZ-2))

def rule_50():
    for x in range(WIDTH//CELL_SZ-1):
        for y in range(HEIGHT // CELL_SZ-1):
            if grid[y, x-1] == 'pink' and grid[y, x+1] == 'pink' or grid[y, x-1] == 'pink'  or grid[y, x+1] == 'pink' :
                grid[y+1, x] = 'pink'




def setup():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rule 50")

def draw():
    clock = pygame.time.Clock()
    running = True
    while running:
        rule_50()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color_bg)
        draw_rect()
        pygame.display.flip()
        clock.tick(30)


setup()
draw()
