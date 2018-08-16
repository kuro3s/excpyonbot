#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット レスポンス格納 クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.2"
__date__    = "2018.8.11"

from common.enums import Switch
from cores.characters import CharacterFactory

class Responser():
    def __init__(self, switch, diff=0.0):

        self._character = CharacterFactory()

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
        self._original_image = self._character._image


    def response(self):
        return [self._name , self._text , self._original_image,self.preview_image]

    @property
    def name(self):
        return self._name

    @property
    def original_image(self):
        return self._original_image

    @property
    def preview_image(self):
        self._preview_image = 'p' + self._character._image
        return self._preview_image

    @property
    def text(self):
        return self._text
