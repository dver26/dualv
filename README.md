# DualV Library

This python library enables you to use dual numbers for automatic differentiation.

You create a function combining the elementary funcions implemented in this library and then differentiate like this:

````
```
import dualv as dv

def f(x):
    return dv.sin(x) + dv.cos(x)

#Derviative in x = 5

x0 = 5

derivative = dv.auto_diff(f, x0)
```
