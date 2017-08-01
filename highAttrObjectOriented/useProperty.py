#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# resolution only readable
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def resolution(self):
        return self._height * self._width

    @width.setter
    def width(self, value):
        self._width = value
    @height.setter
    def height(self, value):
        self._height = value


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
# throw exception
# s.resolution = 233


# set limited value
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance (value, int): 
            raise ValueError('Data type issues.')
        if value > 1000:
            raise ValueError('Data limited issues.')
        self._score = value

stu = Student()
stu.score = 20000


