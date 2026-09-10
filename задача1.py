from math import *

def f(x):
    return (1-x)**0.5 - tan(x)

def g(l, r, esp = 1e-6):
    fl = f(l)
    fr = f(r)
    if fl * fr > 0: #проверка наличия корня
        print("нет корней на отрезке")
        return None
    while abs(r - l) > esp:
        b = (r + l) / 2
        fb = f(b)
        if fl * fb < 0: #проверяем где находится корень
            r = b
            fr = fb
        else:
            l = b
            fl = fb
    return b

l = 0
r = 0.9

root = g(l, r)
print(root)

