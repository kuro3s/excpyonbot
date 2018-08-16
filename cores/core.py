#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コア クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.2"
__date__    = "2018.8.11"

from io import StringIO
from common.enums import Switch
from cores.exccheckers import Excocheckers
from cores.responser import Responser

class Core():
    def __init__(self):
        self._ex = Excocheckers()
        self._buffer = StringIO()

    def buffer(self, _text):
        self._buffer.write(_text)

    def isExc(self,_text=''):
        _result = True
        _buff = self._buffer.getvalue()
        # えくすこたん、えくすこぴょん、はんばーぐ 判定
        try:
            if not _buff == '':
                if self._ex.isExcotan(_buff):
                    _switch = Switch.えくすこたん
                elif self._ex.isExcopyon(_buff):
                    _switch = Switch.えくすこぴょん
                elif self._ex.isHamburg(_buff, _text):
                    _switch = Switch.はんばーぐ
                else:
                    _result = False
        except:
            self._responser = Responser(Switch.例外)
            _result = False

        if _result:
            self._responser = Responser(_switch,self._ex.diff)
            self._buffer = StringIO()

        return _result


    @property
    def Nothing(self):
        return Responser(Switch.Nothing)

    @property
    def responser(self):
        return self._responser
