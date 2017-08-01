#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def printName(self):
        print('age is ', self.__age)
    
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

stu = Student('Spursyy', 20)
# if variable is begin as '__', it sets as private.
# throw exception.
# print(stu.__name) 

stu.printName()
stu.setAge(99)
age = stu.getAge()
print(age)

        
