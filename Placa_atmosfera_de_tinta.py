import numpy as np
from matplotlib import pyplot as plt

def rain():
    return np.random.choice([0, 1], size=(4,4), p=[0.5, 0.5])

x = np.zeros([4,4])
result = x

plt.ion()
fig = plt.figure()
ax = fig.add_subplot()

for i in range(50):
    y = rain()
    result += y
    ax.clear()
    ax.set_title(f'Geração {i}')
    im = ax.imshow(result, cmap='Oranges', vmin=0, vmax=50)  # <-- ESCALA FIXA
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.1)
