import pygame
import numpy as np
from scipy import signal
import sys
import os
from datetime import datetime
# global variables

WIDTH, HEIGHT = 1900, 1000
CELL_SZ = 10
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
grid_w = WIDTH // CELL_SZ
grid_h = HEIGHT // CELL_SZ
generation = 0


def create_grid():
    return np.random.choice([0, 1, 2], size=(grid_h, grid_w), p=[0.4, 0.3, 0.3])


def setup():  # setup
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of segregation")
    return create_grid()


def update(grid):
    # Kernel para contar vizinhos
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    # Contar vizinhos do mesmo tipo
    same_color_neighbors_1 = signal.convolve2d((grid == 1), kernel, mode='same', boundary='wrap')
    same_color_neighbors_2 = signal.convolve2d((grid == 2), kernel, mode='same', boundary='wrap')

    # Nova grade para aplicar mudanças
    new_grid = np.copy(grid)

    # Contadores globais
    # global blue, red
    # blue, red = 0, 0

    # Processar células azuis (1)
    empty_spaces = (grid == 0)  # Inicializar os espaços vazios
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                # blue += 1
                if same_color_neighbors_1[i, j] < 4:  # Não há vizinhos suficientes
                    if empty_spaces.any():  # Existe espaço vazio?
                        new_grid[i, j] = 0  # Esvaziar a célula atual
                        empty_index = np.argwhere(new_grid == 0)  # Recalcular espaços vazios
                        move_to = empty_index[np.random.randint(len(empty_index))]  # Escolher um espaço vazio
                        new_grid[move_to[0], move_to[1]] = 1  # Mover célula azul

    # Recalcular os espaços vazios para as células vermelhas
    empty_spaces = (new_grid == 0)

    # Processar células vermelhas (2)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 2:
                # red += 1
                if same_color_neighbors_2[i, j] < 4:  # Não há vizinhos suficientes
                    if empty_spaces.any():  # Existe espaço vazio?
                        new_grid[i, j] = 0  # Esvaziar a célula atual
                        empty_index = np.argwhere(new_grid == 0)  # Recalcular espaços vazios
                        move_to = empty_index[np.random.randint(len(empty_index))]  # Escolher um espaço vazio
                        new_grid[move_to[0], move_to[1]] = 2  # Mover célula vermelha

    return new_grid



def save_screen(screen):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    current_time = datetime.now()
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    filename = f'screenshots/segregation-{time_str}.png'
    pygame.image.save(screen, filename)


def main():

    grid = setup()  # so puxa o setup
    clock = pygame.time.Clock()  # setar isso pq senão o jogo sai voando
    running = True
    paused = False
    font = pygame.font.Font(None, 36)

    def draw_grid(screen, grid):  # draw so que ele n ta no loop

        global color
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if grid[y, x] == 0:
                    color = (255, 255, 255)  # branco
                elif grid[y, x] == 1:
                    color = (255, 50, 0)  # vermelho
                elif grid[y, x] == 2:
                    color = (0, 50, 255)  # azul
                pygame.draw.rect(screen, color, (x * CELL_SZ + 1, y * CELL_SZ + 1, CELL_SZ - 2, CELL_SZ - 2))

    # loop
    while running:
        global generation
        screen.fill((200, 200, 200))  # preencher em branco igual o processing
        draw_grid(screen, grid)  # puxando a função draw

        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_c:
                    grid = np.zeros((grid_h, grid_w), dtype=int)
                    generation = 0
                elif event.key == pygame.K_r:
                    grid = create_grid()
                    generation = 0
                elif event.key == pygame.K_s:
                    save_screen(screen)
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                if event.button == 1:
                    x, y = event.pos
                    grid_x, grid_y = x // CELL_SZ, y // CELL_SZ
                    grid[grid_y, grid_x] = (grid[grid_y, grid_x] + 1) % 3

        if not paused:
            grid = update(grid)
            generation += 1

        gen_text = font.render(f'Generation: {generation}', True, (0, 0, 0))
        screen.blit(gen_text, (10, 10))

        # gen_text = font.render(f'blue: {blue}', True, (0, 0, 0))
        # screen.blit(gen_text, (10, 30))

        # gen_text = font.render(f'red: {red}', True, (0, 0, 0))
        # screen.blit(gen_text, (10, 50))

        paused_text = font.render("PAUSED" if paused else "RUNNING", True, (255, 0, 0) if paused else (0, 255, 0))
        screen.blit(paused_text, (WIDTH - 120, 10))

        # update frame by frame
        pygame.display.update()
        clock.tick(15)


main()
