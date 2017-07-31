# -*- coding: utf-8 -*-
def f(x):
    return x * x
result = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(result))

result2 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(result2)