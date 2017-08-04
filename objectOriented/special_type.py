#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(isinstance(123, int))

# get all attr and functions
print(dir('abc'))
# the attr or function like '__xxx__' has special usage.

# The len() uses __len__ attr.
print(len('ABC'))
print('ABC'.__len__())


# Custom len() function.
class MyDog(object):
    def __len__(self):
        return 100

myDog = MyDog()
# print 100
print(len(myDog))

# getattr(), setattr(), hasattr()
class MyObject(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getAge(self):
        return self.age

myObject = MyObject("Spursy", 9)
print(hasattr(myObject, 'name'))
setattr(myObject, 'name', 'Wo shi shui.')
print(getattr(myObject, 'name'))


