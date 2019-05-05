#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:11
# @Author  : sakura
# @Site    : 
# @File    : 1-get.py
# @Software: PyCharm


"""
getattribute
描述器的 __get__ 方法 是通过 __getattribute__ 调用的，
实际上，Python 中访问实例属性时，__getattribute__ 就会被调用，
__getattribute__ 会查找整个继承链，直到找到属性，如果没有找到属性，
但是定义了 __getattr__ ，那么就会调用 __getattr__ 去查找属性，
否则抛出 AttributeError
"""

# __getattribute__ 的代码用 Python 实现如下

# def __getattribute__(self, key):
#     val = super().__getattribute__(key)
#     if hasattr(val, '__get__'):
#         return val.__get__(None, self)
#     return val


"""可以做个测试，重写 __getattribute__"""


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return self.name

    def __set__(self, instance, value):
        self.name = value


class C:
    d = Descriptor('d')

    def __getattribute__(self, key):
        if key == 'd':
            val = self.__class__.__dict__['d']
        else:
            val = super().__getattribute__(key)
        if hasattr(val, '__get__'):
            raise AttributeError('NO DESCRIPTOR !!!!!')
        return val


# 访问描述器被 __getattribute__ 拦截了

"""
>>> c.d
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-c1e2befe291e> in <module>()
----> 1 c.d

<ipython-input-1-1c75c3b76140> in __getattribute__(self, key)
     20             val = super().__getattribute__(key)
     21         if hasattr(val, '__get__'):
---> 22             raise AttributeError('NO DESCRIPTOR !!!!!')
     23         return val
     24

AttributeError: NO DESCRIPTOR !!!!!
"""

# data-descriptor and no-data descriptor

"""
如果一个实例只定义了 __get__ 那么，
它就是一个非资料描述器 no-data descriptor ，
如果同时定义了 __get__ 和 __set__ 那么
就是资料描述器 data descriptor
"""

"""
它们的区别在于，如果实例字典中有与描述器同名的属性，
如果是资料描述器，则优先使用资料描述器，否则使用实例字典中的属性
"""


class AbsPriorityDescriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return self.name

    def __set__(self, instance, value):
        self.name = value


class NoPriorityDescriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return self.name


class C:
    a = AbsPriorityDescriptor('a')
    b = NoPriorityDescriptor('b')


# 测试，可以看出来，资料描述器 a 忽略了实例字典的值，而非资料描述器则被覆盖
"""其实类属性和实例属性的底层由此实现原理"""
"""
>>> c = C()
>>> c.a
'a'
>>> c.__dict__['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>> type(c).__dict__['a']
<__main__.AbsPriorityDescriptor object at 0x1091336d8>
>>> c.__dict__['a'] = 'ccccc'
>>> c.a
'a'
>>> c.b
'b'
>>> c.__dict__['b']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'b'
>>> c.__dict__['b'] = 'cccc'
>>> c.b
'cccc'
"""
