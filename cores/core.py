#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コア クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

from common.stringbuilder import StringBuilder
from common.enums import Switch
from cores.responser import Responser
from model.exccheckers import Excocheckers

class Core():
    def __init__(self):
        self._ex = Excocheckers
        self._buffer = StringBuilder()
        self._responser = Responser(Switch.Nothing)

    def stringB(self,_text):
        self._buffer.append(_text)
        print(_text)
        print(self._buffer.toString)


    def _isExc(self, _switch, _text=''):
        _result = False
        _buff = self._buffer.toString
        try:
            if not _buff == '':
                if _switch == Switch.えくすこたん:
                    _result = self._ex.isFullExcotan(_buff)
                elif _switch == Switch.えくすこぴょん:
                    _result = self._ex.isFullExcopyon(_buff)
                elif _switch == Switch.はんばーぐ:
                    _result = self._ex.isFullHamburg(_buff, _text)
                    self._responser = Responser(_switch, self._ex.diff)
                    return _result
        except:
            self._responser = Responser(Switch.例外)
            _result = False

        if _result:
            self._responser = Responser(_switch)

        return _result


    def isExcopyon(self):
        return self._isExc(Switch.えくすこぴょん)

    def isExcotan(self):
        return self._isExc(Switch.えくすこたん)

    def isHamburg(self, text):
        return self._isExc(Switch.はんばーぐ, text)

    @property
    def Nothing(self):
        return Responser(Switch.Nothing)

    @property
    def responser(self):
        return self._responser

