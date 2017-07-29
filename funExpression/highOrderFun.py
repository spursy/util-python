# -*- coding: utf-8 -*-
# 一个函数可以接收另一个函数作为参数，这种函数就称为高阶函数

def add(a, b, f):
    return f(a) + f(b)

result = add(10, -5, abs)
print(result)