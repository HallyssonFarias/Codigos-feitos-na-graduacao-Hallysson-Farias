import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initial population
initial_conditions = [1, 2]  # [rabbits, foxes]
initial_conditions_2 = [4, 5]
# Parameters
a = 1  # rabbits birth rate
b = 1  # rate at which rabbits are eaten
c = 1  # foxes birth rate proportional to rabbits eaten
d = 1  # foxes death rate
k = 5  # limit of food
# A grid of time points (in days)
t = np.linspace(0, 200, 200)


def deriv(y, t, a, b, c, d):  # The differential equations for the predator-prey model.  # adicionar um k aqui
    rabbits, foxes = y
    # print(f"At time {t:.2f}, rabbits = {rabbits:.4f}, foxes = {foxes:.4f}")

    d_rabbits_dt = a * rabbits - b * foxes * rabbits
    # d_rabbits_dt = a * rabbits * (1 - (rabbits/k)) - b * foxes * rabbits
    d_foxes_dt = c * foxes * rabbits - d * foxes
    return [d_rabbits_dt, d_foxes_dt]


# Integrate the equations over the time grid, t.
ret = odeint(deriv, initial_conditions, t, args=(a, b, c, d))  # adicionar um k aqui
ret2 = odeint(deriv, initial_conditions_2, t, args=(a+1, b+1, c+1, d+1))  # adicionar um k aqui

# Split the result into rabbit and fox populations
rabbits, foxes = ret.T
rabbits_2, foxes_2 = ret2.T
# Plot the results
fig1, ax1 = plt.subplots()
ax1.plot(t, rabbits, label="Rabbits")
ax1.plot(t, foxes, label="Foxes")
ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Population')
ax1.legend()
fig2, ax2 = plt.subplots()
ax2.scatter(foxes, rabbits, label='foxes x rabbits', color='b', s=2)
ax2.scatter(foxes_2, rabbits_2, color='r', s=2)
ax2.set_xlabel('foxes')
ax2.set_ylabel('rabbits')
ax2.legend()
plt.show()
