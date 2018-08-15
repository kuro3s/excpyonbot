#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット えくすこメイン
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

from cores.core import Core

class messageAPI():

    def __init__(self):
        self._core = Core()

    def response(self,_text):
        self.__responser = self._core.Nothing

        try:
            self._core.stringB(_text)
            if self._core.isExcopyon() or self._core.isExcotan() or self._core.isHamburg(_text):
                self.__responser = self._core.responser
                self._core = Core()

        except:
            self._core = Core()

        return self.__responser
