#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print("Animal is running")

# inherit run funcion.
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

dog.run()
cat.run()

# overrite parent function.

class Dog1 (Animal):
    def run(self):
        print("dog is running.")

class Cat1 (Animal):
    def run(self):
        print("cat is running.")

dog1 = Dog1()
cat1 = Cat1()
dog1.run()
cat1.run()


# the polymorphic of class
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Cat1())
run_twice(Dog1())



