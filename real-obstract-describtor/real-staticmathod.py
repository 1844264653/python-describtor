#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 0:26
# @Author  : sakura
# @Site    : 
# @File    : real-staticmathod.py
# @Software: PyCharm

"""staticmethod 实现"""


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls=None):
        return self.func
