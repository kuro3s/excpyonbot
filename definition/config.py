#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット コンフィグ クラス
"""
__author__  = "kuro3 <tkoo.xxxxxx@gmail.com>"
__status__  = "production"
__version__ = "0.0.1"
__date__    = "2018.8.11"

from builtins import property
from common.helper import JsonHelper

class Config():

    def __init__(self):
        __source__ = JsonHelper.loader('/bin/config.json')
        self._token = __source__['line']["token"]
        self._secret = __source__['line']["secret"]
        self._static_url = __source__["static_url"]
        self._static_folder = __source__["static_folder"]

    @property
    def token(self):
        return self._token

    @property
    def secret(self):
        return self._secret

    @property
    def static_url(self):
        return self._static_url

    @property
    def static_folder(self):
        return self._static_folder
