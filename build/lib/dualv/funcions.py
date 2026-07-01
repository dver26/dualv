import numpy as np
from .dual import *

def is_dual_close(aprox, truth):
    return abs(aprox.real - truth.real) < 1e-10 and abs(aprox.dual - truth.dual) < 1e-10

def auto_diff(f, x0):
    dual = Dual.diff_dual(x0)
    return f(dual).dual

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

def exp(x):
    if isinstance(x, (int, float)):
        return np.exp(x)
    elif isinstance(x, Dual):
        return Dual(np.exp(x.real), x.dual*np.exp(x.real))
    else:
        return NotImplemented

def ln(x):
    if isinstance(x, (int, float)):
        return np.log(x)
    elif isinstance(x, Dual):
        return Dual(np.log(x.real), x.dual / x.real)
    else:
        return NotImplemented

def sqrt(x):
    if isinstance(x, (int, float)):
        return np.sqrt(x)
    elif isinstance(x, Dual):
        return Dual(np.sqrt(x.real), x.dual/(2*np.sqrt(x.real)))
    else:
        return NotImplemented

def sinh(x):
    return (exp(x)- exp(-x))/2

def cosh(x):
    return (exp(x) + exp(-x))/2

def tanh(x):
    return sinh(x)/cosh(x)
