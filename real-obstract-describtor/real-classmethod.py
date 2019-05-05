#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:27
# @Author  : sakura
# @Site    : 
# @File    : real-classmethod.py
# @Software: PyCharm

"""classmethod 实现"""


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls=None):
        if cls is None:
            cls = type(instance)

        def new_func(*args, **kwargs):
            return self.func(cls, *args, **kwargs)

        return new_func
