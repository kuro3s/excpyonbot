#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット えくすこ判定 クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

import difflib
import unicodedata

class Excocheckers():
    _plist = ['えくすこ','えくすこぴ','えくすこぴょ','えくすこぴょん']
    _tlist = ['えくすこ','えくすこた','えくすこたん']
    _hlist = ['はんばぐ','ハンバグ','ハンバーグ','はんばーぐ','肉']

    diff = 0

    def isExcopyon(value):
        return value in Excocheckers._plist

    def isExcotan(value):
        return value in Excocheckers._tlist

    def isHamburg(value):
        return value in Excocheckers._hlist

    def isFullExcopyon(value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこぴょん' in value or 'エクスコピョン' in value

    def isFullExcotan(value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこたん' in value or 'エクスコタン' in value

    def isFullHamburg(value,text):
        if len(value) <= 6 or text[0] == 'え' or text[0] == 'エ' or text[0] == 'ｴ':
            return False

        _result = False
        _value = unicodedata.normalize('NFKC', value)
        _text = unicodedata.normalize('NFKC', text)
        _dst = _text.translate({
            ord(u'あ'): None,
            ord(u'ア'): None,
            ord(u'ぁ'): None,
            ord(u'ァ'): None,
            ord(u'ー'): None,
            ord(u'！'): None,
            ord(u'？'): None
        })
        for c in Excocheckers._hlist:
            d2 = difflib.SequenceMatcher(None, _dst, c).ratio()
            d1 = difflib.SequenceMatcher(None , _value, c).ratio()
            Excocheckers.diff = max(d1, d2)
            if Excocheckers.diff >= 0.7:
                return True

#            print("d1.{} - {} : {}".format(_value,c,d1))
#            print("d2.{} - {} : {}".format(_dst,c,d2))

        return _result
