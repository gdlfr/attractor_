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
