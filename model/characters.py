#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット キャラクタ生成 クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

import random
from common.jsonloader import loader

class CharacterFactory():

    def __init__(self):
        self.probability = random.choice(list(range(100)))

    def excotan(self):
        """
        えくすこたん 完成時 の 返却用
            1% の確立 で こっしー 召喚
            5% の確立 で えくすこぴょん（ランダム） 召喚
        """
        try:
            if self.probability <= 1:
                self.source = _ksCharacters.source
            elif self.probability > 1 and self.probability <= 6:
                self.source = _exCharacters.source
            else:
                self.source = _etCharacters.source
        except:
            None

        self.__key = random.choice(list(self.source['dictionary'].keys()))
        self.__text = random.choice(self.source['message'])
        self.__image = self.source['dictionary'][self.__key]

    def excopyon(self):
        """
        えくすこぴょん 完成時 の 返却用
            1% の確立 で こっしー を返す
        """
        try:
            if self.probability <= 1:
                self.source = _ksCharacters.source
            else:
                self.source = _exCharacters.source
        except:
            None
        self.__key = random.choice(list(self.source['dictionary'].keys()))
        self.__text = random.choice(self.source['message'])
        self.__image = self.source['dictionary'][self.__key]

    def hamburg(self):
        """
        はんばーぐ 完成時 の 返却用
        """
        try:
            self.source = _hsCharacters.source
        except:
            None
        self.__key = random.choice(list(self.source['dictionary'].keys()))
        self.__text = random.choice(self.source['message'])
        self.__image = self.source['dictionary'][self.__key]

    def qhamburg(self):
        """
        疑わしき はんばーぐ 完成時 の 返却用
        """
        try:
            self.source = _qhsCharacters.source
        except:
            None
        self.__key = random.choice(list(self.source['dictionary'].keys()))
        self.__text = random.choice(self.source['message'])
        self.__image = self.source['dictionary'][self.__key]

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


    @property
    def _name(self):
        return self.__key

    @property
    def _image(self):
        return self.__image

    @property
    def _text(self):
        return self.__text


class _exCharacters(object):
    source = loader('/bin/exp.json')['excopyon']

class _etCharacters(object):
    source = loader('/bin/exp.json')['excotan']

class _ksCharacters(object):
    source = loader('/bin/exp.json')['rice']

class _hsCharacters(object):
    source = loader('/bin/exp.json')['hamburg']

class _qhsCharacters(object):
    source = loader('/bin/exp.json')['qhamburg']