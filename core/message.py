#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット えくすこメイン
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.3"
__date__    = "2018.8.11"

from core.core import Core

class Message():
    def __init__(self):
        self._core = Core()

    def response(self, _id, _text):
        try:
            self._core.buffer(_id, _text)
            if self._core.isExc(_id, _text):
                self._responser = self._core.responser
            else:
                return None
        except:
            return

        return self._responser
