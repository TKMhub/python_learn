# import lesson_package.utils
# r = lesson_package.utils.say_twice('hello')
from lesson_package.talk.human import sing

# 非推奨（どこのモジュールにあるのか分かりずらいため）
from lesson_package.tools.utils import say_twice
r = say_twice('hello')

# 推奨
from lesson_package.tools import utils

r = utils.say_twice('hello')
print(r)

print(sing())