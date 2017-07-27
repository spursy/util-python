# -*- coding: utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product): 
    if num == 1:
        return product
    else:
        return fact_iter(num -1, num * product)

print(fact1(5))
