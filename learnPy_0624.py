print("組み込み関数####################################")
import builtins

print(globals())

builtins.print("組み込み関数")

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print(sorted(ranking, key=ranking.get))
print(sorted(ranking, key=ranking.get, reverse=True))

print("標準ライブラリ####################################")
s = "ngvsfidogvondf"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['f'])

print("サードパーティーのライブラリ####################################")
from termcolor import colored

print('test')
print(colored('test', 'red'))

print(help(colored))

# 非推奨
import collections, sys, os

"""
アルファベット順
かつ
①標準ライブラリ
②サードパーティライブラリ
③開発パッケージ
④ローカルファイル
"""

import collections
import sys
import os

import termcolor

import lesson_package

import config

print(collections.__file__)
print(sys.path)

print("__name__####################################")

import config

import lesson_package.talk.animal

print('lesson：', __name__)

print("クラスとオブジェクト####################################")
s = 'dsifbidfbvdn'
print(s.capitalize())

class Person(object):
    def say_something(self):
        print('hello')

person = Person()
person.say_something()



















