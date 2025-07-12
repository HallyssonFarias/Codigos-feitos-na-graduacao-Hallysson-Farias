import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

def sorteio():
    transition_matrix = np.array([-1, 1])
    result = np.random.choice(transition_matrix, p=[0.5, 0.5])
    return result

x_ax = np.linspace(0,50, 51, dtype=int)
x = np.repeat(0,51)
position = 25

plt.ion()
fig , ax = plt.subplots()
for t in range(50):
    decision = sorteio()
    if decision == 1:
        if 50 >= position + decision >= 0:
            print(f'position, decision: {position, decision}')
            position += 1
            x[position] += 1
            print(f'position + decision: {position}')
        else:
            x[position] += 1
    else:
        if 50 >= position + decision >= 0:
            print(f'position, decision: {position, decision}')
            position -= 1
            x[position] += 1
            print(f'position - decision: {position}')
        else:
            x[position] += 1
    print(x)
    ax.clear()
    ax.set_title(f'tempo: {t}')
    bar = ax.bar(x_ax, height=x)
    ax.set_xlim(0,50)
    ax.set_ylim(0, 15)
    spl = make_interp_spline(x_ax, x, k=3)  # k=3 for cubic spline
    x_ax_line_new = np.linspace(0, 50, 150)
    y_smooth = spl(x_ax_line_new)
    plt.plot(x_ax_line_new, y_smooth, color='r')
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.5)

plt.ioff()
plt.show()
