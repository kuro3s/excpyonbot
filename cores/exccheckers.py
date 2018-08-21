#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット えくすこ判定 クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.3"
__date__    = "2018.8.11"

import difflib
import unicodedata

class Excocheckers():

    def __init__(self):
        self.diff = 0.0

    def isExcopyon(self,value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこぴょん' in _value or 'エクスコピョン' in _value

    def isExcotan(self,value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこたん' in _value or 'エクスコタン' in _value

    def isHamburg(self,value,text):
        _result = False
        _hlist = ['はんばぐ','ハンバグ','肉']
        if text[0] == 'え' or text[0] == 'エ' or text[0] == 'ｴ':
            return _result
        if value.strip(text) == '':
            value = text

        _value = unicodedata.normalize('NFKC', value)
        _text = unicodedata.normalize('NFKC', text)
        _dst = _value.translate({
            ord(u'あ'): None,
            ord(u'ア'): None,
            ord(u'ぁ'): None,
            ord(u'ァ'): None,
            ord(u'ー'): None,
            ord(u'！'): None,
            ord(u'？'): None
        })

        for c in _hlist:
            d2 = difflib.SequenceMatcher(None, _dst, c).ratio()
            d1 = difflib.SequenceMatcher(None , _value, c).ratio()
            self.diff = max(d1, d2)
            print('diff :{} '.format(self.diff))
            if self.diff >= 0.86:
                return True
        return _result
