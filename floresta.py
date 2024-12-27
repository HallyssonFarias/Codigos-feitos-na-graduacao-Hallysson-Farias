import random
import matplotlib.pyplot as plt
import numpy as np
import time
def gerar_floresta(arvores):
    floresta = {}
    # gerando as árvores
    for arvore_c in range(1, arvores + 1):
        floresta[f'arvore_{arvore_c}'] = ['blue', random.randint(0, 50), random.randint(0, 50), 0]
    return floresta, arvores

def gerar_coordenadas(floresta, arvores):
    eixo_x = []
    eixo_y = []
    for eixo in range(0, arvores + 1):
        eixo_x.append(floresta[f'arvore_{eixo}'][1])
        eixo_y.append(floresta[f'arvore_{eixo}'][2])
    return eixo_x, eixo_y

def gerar_cores(floresta, arvores):
    cores = []
    for cor in range(0, arvores + 1):
        cores.append(floresta[f'arvore_{cor}'][0])
    return cores

# gerando floresta
floresta, arvores = gerar_floresta(750)

# gerando o fogo
floresta[f'arvore_0'] = ['red', random.randint(0, 50), random.randint(0, 50), 50]

# gerando eixos
eixo_x, eixo_y = gerar_coordenadas(floresta, arvores)
fig, ax = plt.subplots()
scatter = ax.scatter(eixo_x, eixo_y)
plt.ion()
fig, ax = plt.subplots()

# verificar a distância
for minutos in range(50):
    # gerando cores
    cores = gerar_cores(floresta, arvores)
    # plotagem
    scatter.set_facecolors(cores)

    plt.scatter(eixo_x, eixo_y, color=cores)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.20)
    for k in range(0, arvores + 1):
        for j in range(arvores + 1):
            distancia = 0
            if floresta[f'arvore_{k}'][0] == 'red' and floresta[f'arvore_{j}'][0] != 'red':
                distancia = ( (floresta[f'arvore_{k}'][1]-floresta[f'arvore_{j}'][1])**2 +
                    (floresta[f'arvore_{k}'][2]-floresta[f'arvore_{j}'][2])**2 )**(1/2)
                if distancia <= 3:
                    floresta[f'arvore_{j}'][0]= np.random.choice(['red', 'blue'], p=[0.8,0.2])
                    print(floresta[f'arvore_{j}'])
                    if floresta[f'arvore_{j}'][0] == 'red':
                        print('queimou!')
                    elif floresta[f'arvore_{j}'][0] == 'blue':
                        print('não queimou :D')


plt.ioff()
plt.show()
