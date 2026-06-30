import numpy as np
from .dual import *

def is_dual_close(aprox, truth):
    return abs(aprox.real - truth.real) < 1e-10 and abs(aprox.dual - truth.dual) < 1e-10

def pot(n, x):
    res = 1
    for i in range(n):
        res = res * x
    return res

def sin(x):
    if isinstance(x, (int, float)):
        return np.sin(x)
    elif isinstance(x, Dual):
        return Dual(np.sin(x.real), x.dual*np.cos(x.real))
    else:
        return NotImplemented

def cos(x):
    if isinstance(x, (int, float)):
        return np.cos(x)
    elif isinstance(x, Dual):
        return Dual(np.cos(x.real), -x.dual*np.sin(x.real))
    else:
        return NotImplemented

def tan(x):
    return sin(x)/cos(x)
