#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:19
# @Author  : sakura
# @Site    : 
# @File    : e.g.py
# @Software: PyCharm

"""一些例子说下"""


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise AttributeError('Must be {}'.format(self.ty))
        super().__set__(instance, value)


class Integer(Typed):
    ty = int


class Float(Typed):
    ty = float


class String(Typed):
    ty = str


class Boolean(Typed):
    ty = bool


class Person:
    name = String('name')
    age = Integer('age')


#  测试

"""
>>> c = Person()

>>> c.name = 1
# ignore error
AttributeError: Must be <class 'str'>

>>> c.name = 'aaaa'

>>> c.age = 'aaa'
# ignore error
AttributeError: Must be <class 'int'>

>>> c.age = 18
"""
