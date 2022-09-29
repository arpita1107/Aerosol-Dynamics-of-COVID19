import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from constants import d_water, p_air, T

# function that returns dvx/dt


def model(vx, t, r):
    u = (145 * pow(10, -8) * pow(T, 1.5))/(T + 110.4)
    vis = u/p_air
    Re = (2*vx*r)/vis
    m = d_water * (4/3) * np.pi * pow(r, 3)
    if (Re <= 1):
        k = -(6*p_air*np.pi*pow(r, 2)*vis)/(m*r)
        dvxdt = k * vx
        return dvxdt
    if (Re >= 0.2):
        k2 = -(0.5*21.12*np.pi*pow(r, 2)*p_air*vis)/(2*m*r)
        k2 = -(0.5*21.12*np.pi*pow(r, 2)*p_air*vis)/(2*m*r)
        k3 = -(0.5*6.3*p_air*np.pi*pow(r, 2)*pow(vis, 0.5))/(m*pow((2*r), 0.5))
        k4 = -(0.5*0.25*p_air*np.pi*pow(r, 2))/m
        dvxdt = (k2 * vx) + (k3 * pow(vx, 1.5)) + (k4 * pow(vx, 2))
        return dvxdt


# time points
t = np.linspace(0, 0.0001, 5)
dt = t[1] - t[0]
r = 10 * pow(10, -6)

sol = np.zeros(5)

# initial condition
sol[0] = 50

# solve ODE
for i in range(1, 5):
    sol[i] = sol[i-1] + dt*model(sol[i-1], t[i-1], r)


plt.plot(t, sol, color='blue', label='Diameter = 10µm')


r = 5 * pow(10, -6)
for i in range(1, 5):
    sol[i] = sol[i-1] + dt*model(sol[i-1], t[i-1], r)


plt.plot(t, sol, color='red', label='Diameter = 5µm')

plt.ylabel('vx[m/s]')
plt.xlabel('t[s]')
plt.legend(loc='best')
plt.show()

# k = -(6*p_air*np.pi*pow(r,2)*vis)/(m*r)

# # k2 = -(0.5*21.12*np.pi*r*u)/(2*m)
# # k3 = -(0.5*6.3*pow(p_air, 0.5)*np.pi*pow(r, 2)
# #        * pow(u, 0.5))/(m*pow(r, 0.5)*pow(2, 0.5))
# # k4 = -(0.5*0.25*p_air*np.pi*pow(r, 2))/m
# # dvxdt = (k2 * vx) + (k3 * pow(vx, 1.5)) + (k4 * pow(vx, 2))
# dvxdt = k * vx
# return dvxdt
