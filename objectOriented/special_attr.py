#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
# <__main__.Student object at 0x004C0210>
print(Student('Spursyy'))

# use __str__
class Teacher(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Teacher object is %s" % self.name
    __repr__ = __str__
# Teacher object is 'YY'.
print(Teacher('YY'))


# __iter__ and __next__
class Fib(object):
    # def __init__(self):
    #     self.a = 0
    #     self.b = 1
    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     self.a, self.b = self.b, self.a + self.b
    #     if (self.a > 20000):
    #         raise StopIteration()
    #     return self.a

# for n in Fib():
#     print(n)

    # __getitem__: transform to list
    def __getitem__(self,n):
        if isinstance(n, int):
            a,b = 1,1
            for x in range(n):
                a, b = b, a + b
                # print(a)
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop

            if start is None:
                start = 0
            a,b = 1,1

            for x in range(stop):
                a,b = b, a + b
            return a

f = Fib()
# print(f[1])   
print(f[:10])


# __getattr__ difine attribute not in __init__ func
class Person(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if (attr == 'age'):
            return 35
        raise AttributeError('no %s attribute.' % attr)

people = Person("Spursyy")
print(people.age)


# __call__ define instance func and identify attr in object or not.

class Person1(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('my nane is %s' % self.name)

person1 = Person1("tianMa")
person1()

# true
print(callable(Person1))
# false
print(callable([1,2,3]))






