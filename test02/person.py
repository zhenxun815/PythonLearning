#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description:
# @File: Person.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/4/7 20:14


class Person:
    # Class variables,only one copy, all instances share
    population = 0

    def __init__(self, name, age):
        # Object variable,owned by each individual instance
        # An object variable with the same name as a class variable will hide the class variable!
        self.name = name
        self.age = age
        print("Initializing with name: {}, age: {}".format(self.name, self.age))
        Person.population += 1

    def die(self):
        print("{} is going to die!".format(self.name))

        Person.population -= 1
        if Person.population == 0:
            print("{} was the last one...".format(self.name))
        else:
            print("There are still {:d} living person.".format(Person.population))
            # print("There are still {:d} living person.".format(self.__class__.population))

    def say_hi(self):
        print('Name is:', self.name)

    @classmethod
    def how_many(cls):
        print("Person population is {:d}".format(cls.population))



