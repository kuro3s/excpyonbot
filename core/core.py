#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コア クラス
"""
__author__ = 'kuro3 <tkoo.xxxxxx@gmail.com>'
__status__ = 'production'
__version__ = '0.1.0'
__date__ = '2018.8.22'

import difflib
import unicodedata
import random

from io import StringIO
from common.helper import (Switch, loader)

__ratio_value__ = float(loader(path='/bin/config.json')["ratio_value"])


class Core:
    def __init__(self):
        self._ex = ExcChecker()
        self._dictionary = {}
        self._response = Response(Switch.Nothing)

    def buffer(self, _id, _text):
        _buff = StringIO()

        if _id in self._dictionary.keys():
            _buff.write(self._dictionary[_id])

        _buff.write(_text)
        self._dictionary[_id] = _buff.getvalue()
        print(_id + ':' + _text + '(buff :' + _buff.getvalue() + ')')

    def isExc(self, _id, _text=''):
        _result = True
        _buff = self._dictionary[_id]
        _switch = Switch.Nothing
        # えくすこたん、えくすこぴょん、はんばーぐ 判定
        try:
            if not _buff == '':
                if self._ex.isExcotan(_buff, _text):
                    _switch = Switch.えくすこたん
                elif self._ex.isExcopyon(_buff, _text):
                    _switch = Switch.えくすこぴょん
                elif self._ex.isHamburg(_buff, _text):
                    _switch = Switch.はんばーぐ
                elif self._ex.isOtherwise(_buff, _text):
                    _switch = Switch.その他
                else:
                    _switch = Switch.例外
                    _result = False

        except:
            self._response = Response(Switch.例外)
            _result = False

        if _result:
            self._response = Response(_switch, self._ex.diff)
            self._dictionary.pop(_id)
            print('diff : {}'.format(self._ex.diff))

        return _result

    @property
    def response(self):
        return self._response


class Response:
    def __init__(self, _switch, _diff=0.0):
        self._character = CharacterFactory()

        if _switch == Switch.えくすこぴょん:
            self._character.excopyon()
        elif _switch == Switch.えくすこたん:
            self._character.excotan()
        elif _switch == Switch.はんばーぐ:
            if _diff > 0.8:
                self._character.hamburg()
            else:
                self._character.qhamburg()
        elif _switch == Switch.その他:
            self._character.otherwise()
        elif _switch == Switch.Nothing:
            self._character.nothing()
        else:
            self._character.exception()

    @property
    def list(self):
        return [self._character.name, self._character.text, self._character.image]

    @property
    def name(self):
        return self._character.name

    @property
    def original_image(self):
        return self._character.image

    @property
    def preview_image(self):
        return 'p' + self._character.image

    @property
    def text(self):
        return self._character.text


class ExcChecker:
    NFKC = 'NFKC'

    def __init__(self):
        self.diff = 0.0

    def isExcCharacter(self, _clist, _buff, _text):
        _result = False

        _BUFF = unicodedata.normalize(ExcChecker.NFKC, _buff)
        _TEXT = unicodedata.normalize(ExcChecker.NFKC, _text)

        if _BUFF.strip(_TEXT) == '':
            _BUFF = _TEXT

        _COMP =_BUFF.translate({
            ord(u'あ'): None,
            ord(u'ア'): None,
            ord(u'ぁ'): None,
            ord(u'ァ'): None,
            ord(u'ー'): None,
            ord(u'!'): None,
            ord(u'?'): None
        })
        print(_COMP)

        for c in _clist:
            _d1 = difflib.SequenceMatcher(None, _COMP, c).ratio()
            _d2 = difflib.SequenceMatcher(None, _TEXT, c).ratio()
            _d3 = difflib.SequenceMatcher(None, _TEXT, 'おいで'+c).ratio()
            self.diff = max(_d1, _d2, _d3)
            print('diff :{} '.format(self.diff))
            if self.diff >= __ratio_value__:
                return True

        return _result


    def isExcopyon(self, _buff, _text):
        _BUFF = unicodedata.normalize(ExcChecker.NFKC, _buff)
        _COMP =_BUFF.translate({
            ord(u'ー'): None,
            ord(u'!'): None,
            ord(u'?'): None
        })
        print(_COMP)
        if 'えくすこぴょん' in _COMP or 'エクスコピョン' in _COMP:
            _clist = ['えくすこぴょん', 'エクスコピョン']
            return self.isExcCharacter(_clist, _buff, _text)
        else:
            return False

        _clist = ['えくすこぴょん', 'エクスコピョン']
        return self.isExcCharacter(_clist, _buff, _text)


    def isExcotan(self, _buff, _text):
        _BUFF = unicodedata.normalize(ExcChecker.NFKC, _buff)
        _COMP =_BUFF.translate({
            ord(u'ー'): None,
            ord(u'!'): None,
            ord(u'?'): None
        })
        print(_COMP)
        if 'えくすこたん' in _COMP or 'エクスコタン' in _COMP:
            _clist = ['えくすこたん', 'エクスコタン']
            return self.isExcCharacter(_clist, _buff, _text)
        else:
            return False

    def isHamburg(self, _buff, _text):
        _clist = ['はんばぐ', 'ハンバグ', '肉', 'にく', '師匠']
        return self.isExcCharacter(_clist, _buff, _text)

    def isOtherwise(self, _buff, _text):
        _clist = ['すこ','すこすこ', '米', 'お米を食べよう', 'こっし', 'こしひかり']
        return self.isExcCharacter(_clist, _buff, _text)


class CharacterFactory:
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
        _cls = self.Excotan()
        if self.probability <= 1:
            _cls = self.Otherwise()
        self.setter(_cls)

    def excopyon(self):
        """
        えくすこぴょん 完成時 の 返却用
            1% の確立 で こっしー を返す
        """
        _cls = self.Excopyon()
        if self.probability <= 1:
            _cls = self.Otherwise()
        self.setter(_cls)

    def hamburg(self):
        """
        はんばーぐ 完成時 の 返却用
        """
        self.setter(self.Hamburg())

    def qhamburg(self):
        """
        疑わしき はんばーぐ 完成時 の 返却用
        """
        self.setter(self.Qhamburg())

    def otherwise(self):
        """
        その他
        """
        self.setter(self.Otherwise())

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
    def name(self):
        return self.__key

    @property
    def text(self):
        return self.__text

    @property
    def image(self):
        return self.__image

    class Excopyon(object):
        source = loader(path='/bin/exp.json')['excopyon']

    class Excotan(object):
        source = loader(path='/bin/exp.json')['excotan']

    class Hamburg(object):
        source = loader(path='/bin/exp.json')['hamburg']

    class Qhamburg(object):
        source = loader(path='/bin/exp.json')['qhamburg']

    class Otherwise(object):
        source = loader(path='/bin/exp.json')['otherwise']

