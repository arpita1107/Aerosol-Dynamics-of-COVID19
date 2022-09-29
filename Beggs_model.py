import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from constants import kv, kd, pv

# function that returns di/dt
def model(c0, t):
    ct = c0 * np.exp(-(kv*t))
    didt = pv * ct
    return didt


# def conc(c0, t):
#     c1 = c0 * np.exp(t)
#     return c1


# time points
t = np.linspace(0, 1.0)
c0 = 0.001626

# solv ODE
y = odeint(model, c0, t)

# plot results
plt.plot(t, y, color='blue', label='Particles inhaled(speaking simulation)')
c0 = 0.000441
y = odeint(model, c0, t)
plt.plot(t, y, color='green', label='Particles inhaled(coughing simulation)')
plt.xlabel('time [s]')
plt.ylabel('droplets inhaled [N]')
plt.legend()
plt.show()

# c = odeint(conc, c0, t)
# plt.plot(t, c, color='red', label='Particle conc.')
