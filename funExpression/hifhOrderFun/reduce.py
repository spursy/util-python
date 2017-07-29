# -*- coding: utf-8 -*-
def add(x, y):
    return x + y
result = reduce(add, [1,2,3,4,5,6,7])
# 28
print(result)

# '987654' convert to 987654
def fn(x, y):
    return x * 10 + y
def charInNumbers(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

result2 = reduce(fn, map(charInNumbers, '987654'))
print(result2)

# put all fun encapsulate a whole fun.
def strToInt(s):
    def fn2(x, y):
        return x * 10 + y
    def charInNumbers2(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':    6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn2, map(charInNumbers2, s))

result3 = strToInt('198507428892')
print(result3)

#use lambda to make fun concise
def strToInt2(s):
    def charInNumbers3(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':    6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(charInNumbers3, s))

result4 = strToInt2('9999999999999')
print(result4)

# define a function to calculate multiplication
def multiplicate(L):
    return reduce(lambda x, y : x * y, L)

result5 = multiplicate([2,4,5,6,7])
print(result5)