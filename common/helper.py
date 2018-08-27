#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット helper クラス
"""
__author__ = 'kuro3 <tkoo.xxxxxx@gmail.com>'
__status__ = 'production'
__version__ = '0.0.1'
__date__ = '2018.8.22'

import os
import json
import codecs
from enum import Enum


# class JsonHelper(object):

def writer(path, value):
    with codecs.open(os.getcwd() + path, 'w', 'utf-8_sig') as f:
        dump = json.dumps({value}, ensure_ascii=False)
        f.write(dump)
        f.close()


def loader(path):
    f = open(os.getcwd() + path, 'r', encoding='utf-8_sig')
    data = json.load(f)

    f.close()
    return data


class Switch(Enum):
    Nothing = 0
    えくすこぴょん = 1
    えくすこたん = 2
    はんばーぐ = 3
    その他 = 4
    例外 = 9
