#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コア クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.3"
__date__    = "2018.8.11"

from io import StringIO
from common.enums import Switch
from cores.exccheckers import Excocheckers
from cores.responser import Responser

class Core():
    def __init__(self):
        self._ex = Excocheckers()
        self._dictionary = {}

    def buffer(self, _id,_text):
        _buff = StringIO()

        if _id in self._dictionary.keys():
            _buff.write(self._dictionary[_id])

        _buff.write(_text)
        self._dictionary[_id] = _buff.getvalue()
        print(_id + ':' + _text + '(buff :' + _buff.getvalue()+')')

    def isExc(self,_id,_text=''):
        _result = True
        _buff = self._dictionary[_id]
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
            self._dictionary.pop(_id)
            print('diff : {}'.format(self._ex.diff))

        return _result


    @property
    def Nothing(self):
        return Responser(Switch.Nothing)

    @property
    def responser(self):
        return self._responser
