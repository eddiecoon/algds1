from math import *

def f(x):
    return (1-x)**0.5 - tan(x)

def g(a, b, eps = 1e-6):
    fa = f(a)
    fb = f(b)
    x = [0] * 100
    for k in range(100): #метод хорд
        x[k] = a - (fa * (b-a))/(fb - fa)
        fk = f(x[k])
        if fk == 0:
            return x[k]
        if fk * fb > 0:
            b = x[k]
            fb = fk
        else:
            a = x[k]
            fa = fk
        if k > 0 and abs(x[k] - x[k-1]) < eps:
            return x[k]

root = g(0, 0.9)

print(root)