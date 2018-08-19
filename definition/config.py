#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コンフィグ クラス
"""
from builtins import property
from common.jsonloader import loader

__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"


class Config():

    def __init__(self):
        __source = loader('/bin/line.json')
        self._token = __source["token"]
        self._secret = __source["secret"]

    @property
    def token(self):
        return self._token

    @property
    def secret(self):
        return self._secret
