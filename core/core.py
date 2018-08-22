#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コア クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.1.0"
__date__    = "2018.8.22"

import difflib
import unicodedata
import random

from io import StringIO
from common.helper import (Switch, JsonHelper)

class Core():
    def __init__(self):
        self._ex = __excochecker__()
        self._dictionary = {}

    def buffer(self, _id, _text):
        _buff = StringIO()

        if _id in self._dictionary.keys():
            _buff.write(self._dictionary[_id])

        _buff.write(_text)
        self._dictionary[_id] = _buff.getvalue()
        print(_id + ':' + _text + '(buff :' + _buff.getvalue()+')')

    def isExc(self, _id, _text=''):
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
            self._responser = __responser__(Switch.例外)
            _result = False

        if _result:
            self._responser = __responser__(_switch, self._ex.diff)
            self._dictionary.pop(_id)
            print('diff : {}'.format(self._ex.diff))

        return _result

    @property
    def Nothing(self):
        return __responser__(Switch.Nothing)

    @property
    def responser(self):
        return self._responser


class __responser__():
    def __init__(self, switch, diff=0.0):
        self._character = __characterFactory__()

        if switch == Switch.えくすこぴょん:
            self._character.excopyon()
        elif switch == Switch.えくすこたん:
            self._character.excotan()
        elif switch == Switch.はんばーぐ:
            if diff > 0.8:
                self._character.hamburg()
            else:
                self._character.qhamburg()
        elif switch == Switch.Nothing:
            self._character.nothing()
        else:
            self._character.exception()

        self._name = self._character._name
        self._text = self._character._text
        self._image = self._character._image

    @property
    def name(self):
        return self._name

    @property
    def original_image(self):
        return self._image

    @property
    def preview_image(self):
        return 'p' + self._character._image

    @property
    def text(self):
        return self._text


class __excochecker__():
    def __init__(self):
        self.diff = 0.0

    def isExcopyon(self, value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこぴょん' in _value or 'エクスコピョン' in _value

    def isExcotan(self, value):
        _value = unicodedata.normalize('NFKC', value)
        return 'えくすこたん' in _value or 'エクスコタン' in _value

    def isHamburg(self, value, text):
        _result = False
        _hlist = ['はんばぐ','ハンバグ','肉']
        if text[0] == 'え' or text[0] == 'エ' or text[0] == 'ｴ':
            return _result
        if value.strip(text) == '':
            value = text

        _value = unicodedata.normalize('NFKC', value)
        _text = unicodedata.normalize('NFKC', text)
        _dst =_value.translate({
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
            d1 = difflib.SequenceMatcher(None, _value, c).ratio()
            self.diff = max(d1, d2)
            print('diff :{} '.format(self.diff))
            if self.diff >= 0.86:
                return True
        return _result


class __characterFactory__():
    def __init__(self):
        self.probability = random.choice(list(range(100)))
        self.__key = None
        self.__text = None
        self.__image = None

    def excotan(self):
        """
        えくすこたん 完成時 の 返却用
            1% の確立 で こっしー 召喚
            5% の確立 で えくすこぴょん（ランダム） 召喚
        """
        try:
            _cls = __etCharacters__
            if self.probability <= 1:
                _cls = __ksCharacters__
            elif self.probability > 1 and self.probability <= 6:
                _cls = __exCharacters__

        except:
            None

        self.setter(_cls)

    def excopyon(self):
        """
        えくすこぴょん 完成時 の 返却用
            1% の確立 で こっしー を返す
        """
        try:
            _cls = __ksCharacters__
            if not self.probability <= 1:
                _cls = __exCharacters__
        except:
            None
        self.setter(_cls)

    def hamburg(self):
        """
        はんばーぐ 完成時 の 返却用
        """
        try:
            _cls = __hsCharacters__
        except:
            None
        self.setter(_cls)

    def qhamburg(self):
        """
        疑わしき はんばーぐ 完成時 の 返却用
        """
        try:
            _cls = __qhsCharacters__
        except:
            None
        self.setter(_cls)

    def exception(self):
        """
        例外 返却用
        """
        self.__key = '例外'
        self.__text = '例外エラーが発生しました。\n' + 'メンテナンス中です...'
        self.__image = None

    def nothing(self):
        """
        Nothing
        :return:
        """
        self.__key = None
        self.__text = None
        self.__image = None

    def setter(self, _cls):
        self.__key = random.choice(list(_cls.source['dictionary'].keys()))
        self.__text = random.choice(_cls.source['message'])
        self.__image = _cls.source['dictionary'][self.__key]

    @property
    def _name(self):
        return self.__key

    @property
    def _text(self):
        return self.__text

    @property
    def _image(self):
        return self.__image



class __exCharacters__(object):
    source = JsonHelper.loader('/bin/exp.json')['excopyon']


class __etCharacters__(object):
    source = JsonHelper.loader('/bin/exp.json')['excotan']


class __ksCharacters__(object):
    source = JsonHelper.loader('/bin/exp.json')['rice']


class __hsCharacters__(object):
    source = JsonHelper.loader('/bin/exp.json')['hamburg']


class __qhsCharacters__(object):
    source = JsonHelper.loader('/bin/exp.json')['qhamburg']

