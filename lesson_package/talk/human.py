# 絶対パス→　推奨
# from lesson_package.tools import utils
# 相対パス→　非推奨
from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')