#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:05
# @Author  : 海心
# @Site    : 
# @File    : python_describtor.py
# @Software: PyCharm


"""
描述器
Python 有三个特殊方法，__get__、__set__、__delete__，用于覆盖属性的一些默认行为，
如果一个类定义了其中一个方法，那么它的实例就是描述器
"""


# 下面是一个简单的描述器的示例，Descriptor 是一个实现了 __get__、__set__ 的类，可以为其实例访问和修改时打印信息

class Descriptor:
    def __init__(self, initvar=None, name='var'):
        self.initvar = initvar
        self.name = name

    def __get__(self, instance, cls):
        print('Get', self.name)
        return self.initvar

    def __set__(self, instance, value):
        print('Set', self.name, value)
        self.initvar = value


class E:
    a = Descriptor(10, 'a')
    b = Descriptor(20, 'b')


"""
>>> e = E()
>>> e.a
Get a
10
>>> e.b
Get b
20
>>> e.b = 10
Set b 10
>>> e.b = 30
Set b 30
"""

"""描述器是一种代理机制，对属性的操作由这个描述器来代理"""

"""
访问: __get__(self, instance, cls) # instance 代表实例本身，cls 表示类本身，使用类直接访问时，instance 为 None
赋值: __set__(self, instance, value) # instance 为实例，value 为值
删除: __delete__(self, instance) # instance 为实例
"""


# 下面这个例子列出了不同情况下 instance 和 cls 的值

class TestDescriptor:
    def __get__(self, instance, cls):
        print('instance', instance)
        print('class', cls)

    def __set__(self, instance, value):
        print(instance)

    def __delete__(self, instance):
        print(instance)


class F:
    f = TestDescriptor()


"""
>>> f = F()
>>> f.f
instance <__main__.F object at 0x10ff2fa20>
class <class '__main__.F'>
>>> f.f = 'c'
<__main__.F object at 0x10ff2fa20>
>>> del f.f
<__main__.F object at 0x10ff2fa20>
>>> F.f
instance None
class <class '__main__.F'>
"""
