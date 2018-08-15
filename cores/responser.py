#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット レスポンス格納 クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

from model.characters import CharacterFactory
from common.enums import Switch

class Responser():
    def __init__(self, switch, diff=0.0):

        self.__character = CharacterFactory()

        if switch == Switch.えくすこぴょん:
            self.__character.excopyon()
        elif switch == Switch.えくすこたん:
            self.__character.excotan()
        elif switch == Switch.はんばーぐ:
            if diff > 0.8:
                self.__character.hamburg()
            else:
                self.__character.qhamburg()
        elif switch == Switch.Nothing:
            self.__character.nothing()
        else:
            self.__character.exception()

        self.__name = self.__character._name
        self.__text = self.__character._text
        self.__original_image = self.__character._image


    def response(self):
        return [self.__name , self.__text , self.__original_image,self.__preview_image]

    @property
    def name(self):
        return self.__name

    @property
    def original_image(self):
        return self.__original_image

    @property
    def preview_image(self):
        self.__preview_image = 'p' + self.__character._image
        return self.__preview_image

    @property
    def text(self):
        return self.__text
