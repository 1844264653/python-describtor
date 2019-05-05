#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:24
# @Author  : sakura
# @Site    : 
# @File    : real-describtor.py
# @Software: PyCharm

"""property 的实现"""

"""
虽然 property 是 C 代码实现的，但是我们可以模拟出 Python 的 Property
"""


class Property:
    def __init__(self, fget, fset=None, fdel=None):  # no defined fdoc
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('can not set')
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('can not delete')
        self.fdel(instance)

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self


"""使用自定义的 Property"""


class A:
    def geta(self):
        return self._a

    def seta(self, value):
        self._a = value

    def dela(self):
        del self._a

    a = Property(fget=geta, fset=seta, fdel=dela)
