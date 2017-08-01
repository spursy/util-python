#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# when we instance a class, system can bind any func or attrs, It is very flexible.
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printName(self):
        print(self.name)

stu = Student("Spursy", 30)

stu.grade = 'grade 2'
# print grade2
print(stu.grade)

# bind function
def setName(self, name):
    self.name = name

from types import MethodType
stu.setName = MethodType(setName, stu)
stu.setName("YY")

print(stu.name)

# use __slots__ to limit arr
class Animal(object):
    # use tuple type
    __slots__ = ("name", "age")

animal = Animal()
# throw exception
animal.grade = "VIP"





