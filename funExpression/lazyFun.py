# -*- coding: utf-8 -*-

def cal_Sum(*args):
    sum= 0 
    for n in args:
        sum = sum + n
    return sum

result = cal_Sum(1,2,3,4,5)
print(result)

# Lazy sum function
def lazy_Sum(*args):
    def cal_Sum():
        sum = 0
        for n in args:
            sum = sum + n
        return sum
    return cal_Sum

result2 = lazy_Sum(1,3,5,7,9)
print(result2())

# closure

def count():
    fs = []
    for n in range(1, 4):
        def f():
            return n * n
        fs.append(f) 

    return fs

f1, f2, f3 = count()
# 9
print(f1())
# 9  
print(f2())
# 9
print(f3())


def count1():
    fs = []
    def f(n):
        def g():
            return n * n
        return g;
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f4, f5, f6 = count1()
# 1
print(f4())
# 4  
print(f5())
# 9
print(f6())
