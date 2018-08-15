#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット Stringbuilder クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

class StringBuilder():

    def __init__(self):
        self._list = ['']

    def append(self,value):
        self._list.append(value)

    def appenLine(self,value):
        self._list.append(value.join('\n'))

    def isNullorEmpty(self):
        return self.toString == ''

    @property
    def toString(self):
        _result = ''
        if not self._list.count is 0:
            _result = "".join(self._list)
        return _result

