# -*- coding: utf-8 -*-

def power(x):
    return x * x
print(power(5))


def power2(x ,n):
    s = 1
    while(n > 0):
        s = s * x
        n = n - 1
    return s
print(power2(4, 3))

def power3(x ,n = 3):
    s = 1
    while(n > 0):
        s = s * x
        n = n - 1
    return s
print(power3(4))
print(power3(4, 4))


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc([1,2,3,4,5]))
print(calc((1,2,3,4,5, 6)))

# 可变参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc2(1,2,3))

# 关键字参数
def person(name, age, **kw): 
    print('Name:', name, 'Age', age, 'Others', kw)

person('Spursy', 25) 
person('Spursy', 25, city = 'BeiJing')
person('Spursy', 25, city = 'BeiJing', gentle = 'boy')

extra = {'city': 'BeiJing', 'gentle': 'boys'}
person('Spursy', 25, **extra) 

# 命名关键字参数
def person2(name, age, **kw):
    if 'city' in kw:
        return
    if 'gentle1' in kw:
        pass
    print('Name:', name, 'Age', age, 'Others', kw) 

extra2 = {'city': 'ShangHai', 'gentle1': 'boys'}
person2('YY', '35', **extra2)
person2('YY', 25, city = 'BeiJing', gentle1 = 'boy')


def person3(name, age, *, city, job):
    print(name, age, city, job)
person3("YY01", 80, city='ShangHai', job = 'IT')

def person4(name, age, *arg, city, job):
    print(name, age,arg, city, job)

person4("YY01", 80,'ShangHai', 'IT', city='ShangHai', job = 'IT')
