# -*- coding: utf-8 -*-

def f(x):
    return x * x

result1 = map(f, [1,2,3,4,5,6,7,8,9])
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(result1) 

L = []
for n in [1,2,3,4,5,6,7]:
    L.append(f(n))
print(L)


# Homework
# convert ['adam', 'LISA', 'barI'] to ['Adam', 'lisa', 'Barl']

def normalize(name):
    return name.capitalize()

result2 = list(map(normalize, ['adam', 'LISA', 'barI']))
print(result2)

