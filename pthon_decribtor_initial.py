#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:02
# @Author  : 海心
# @Site    : 
# @File    : pthon_decribtor_initial.py
# @Software: PyCharm

"""我们可以使用 Python 自带的 property 装饰器 来控制属性的访问，
下面这个例子通过 property 控制了 Person 的 age 属性的访问和修改"""


class Person:

    def __init__(self, name=None, age=None):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise AttributeError('Must be {}'.format(int))
        if value > 200:
            raise AttributeError('Value Must < 200')
        self._age = value


"""试一试，的确如代码写的一样，对属性的类型进行了检查，而且使用了 property 装饰器之后，
对 age 方法的访问和对属性的访问一样，不需要加 ()"""


"""
>>> a = Person()
>>> a.age
>>> a.age = 10
>>> a.age
10
>>> a.age = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "person.py", line 14, in age
    raise AttributeError('Must be {}'.format(int))
AttributeError: Must be <class 'int'>
>>> a.age = 201
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "person.py", line 16, in age
    raise AttributeError('Value Must < 200')
AttributeError: Value Must < 200
"""


