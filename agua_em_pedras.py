import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def setup():
    return np.random.choice([0, 1], size=(50, 50), p=[0.7, 0.3])

def update(grid):
    new_grid = grid.copy()
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if grid[i][j] == 0:  # só pode virar água se for espaço vazio
                if (grid[i-1][j] == 2 or # cima
                    grid[i+1][j] == 2 or # baixo
                    grid[i][j-1] == 2 or # esquerda
                    grid[i][j+1] == 2): # direita
                    new_grid[i][j] = 2
    return new_grid

# Cores: areia, pedra, água
colors = ['#EEDD82', '#808080', '#1E90FF']
cmap = matplotlib.colors.ListedColormap(colors)


x = setup()
x[0] = 2 # transformar so em cima em água

plt.ion()
fig, ax = plt.subplots()

for g in range(70):
    x = update(x)
    ax.clear()
    ax.set_title(f'Difusão da água - Geração {g}')
    ax.imshow(x, cmap=cmap, vmin=0, vmax=2)
    plt.pause(0.2)

plt.ioff()
plt.show()
