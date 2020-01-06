import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go


### solving the equation system ###

# system of equations:
def LorenzMod1(XYZ, t, alpha, beta, xi, delta):
    x, y, z = XYZ
    x_dt = -alpha*x + y*y - z*z + alpha*xi
    y_dt = x*(y - beta*z) + delta
    z_dt = -z + x*(beta*y + z)
    return x_dt, y_dt, z_dt

# system parameters and startup conditions:
alpha = 0.1
beta = 4
xi = 14
delta = 0.08

# max time and quantity of time points:
tmax, n = 100, 50000

# integrate the system of equations at each point of the time interval t:
t = np.linspace(0, tmax, n)
f = odeint(LorenzMod1, (x_0, y_0, z_0), t, args=(alpha, beta, xi, delta))
X, Y, Z = f.T

