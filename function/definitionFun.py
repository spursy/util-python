# -*- coding: utf-8 -*-

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-10))


def nop():
    pass


def my_abs1(x):
    if not isinstance (x , (int, float)):
        raise TypeError('Value type is not mapping.')
    if x > 0:
        return x
    else:
        return -x

print(my_abs1(-10))
# print(my_abs1('ASD'))


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6);
print(x, y)