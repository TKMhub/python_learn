print("zip関数####################################")
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

print("辞書型for####################################")
d = {'x': 100, 'y': 200}
print(d.items())
for k, v in d.items():
    print(k,':',v)

print("関数####################################")
def say_something():
    print('hi')

say_something()

f = say_something
f()

def say_something2():
    s = 'hello'
    return s

result = say_something2()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    else:
        return 'grape'

result = what_is_this('red')
print(result)
result = what_is_this('blue')
print(result)

# エラーは返してくれない！
num: int = 10
def add_num(a: int, b: int) -> int:
    return a + b

add_num(10, 20)

def menu(entry, drink, dessert):
    print(entry)
    print(drink)
    print(dessert)
# 順番が大切
menu(entry='beef', drink='beer', dessert='ice')

def menu(entry='beef', drink='beer', dessert='ice'):
    print(entry)
    print(drink)
    print(dessert)

#デフォルト引数を上書き
menu(entry='chicken')

# def test_func(x, l=[]):
#     l.append(x)
#     return l

# y = [1,2,3]
#
# print(test_func(100, y))
# print(test_func(200, y))

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

y = [1,2,3]
# バグに繋がる
print(test_func(100))
print(test_func(100))
print(test_func(200, y))

# 複数の引数を一括で受け取りたい時は「*args」
# →タプルに入れてくれる
def say_something(*args):
    print(args)

say_something('Hi', 'Mike', 'Nance')

def say_something2(word, *args):
    print('word:', word)
    for arg in args:
        print(arg)

# ↓あまり使われない
t = ('Mike', 'Nancy')
say_something2('Hi', *t)


# def menu(entree='beef', drink='wine'):
#     print(entree, drink)
#
# menu(entree='beef', drink='cofee')

# **kwargs
# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k,v)
#
# menu(entree='beef', drink='cofee')

# def menu(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k,v)
#
# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }
#
# menu(**d)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orrange', entree='beef', drink='coffee' )

def menu(food, *args, **kwargs):
    """
    パイソンのドキュメントは関数の中にある
    :param food:
    :param args:
    :param kwargs:
    :return:
    """
    print(food)
    print(args)
    print(kwargs)

print("関数内関数####################################")
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1)
    print(r2)

outer(1, 2)

print("クロージャー####################################")
#はじめに設定した引数をもとに、後々用途によって使い分けたい時に使う。

# def outer(a, b):
#
#     def inner():
#         return a + b
#
#     return inner
#
# # アウター実行開始
# print(outer(1, 2))
# # インナー実行開始
# f = outer(1, 2)
# r = f()
# print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print("デコレータ####################################")

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, *kwargs)
        print('end')
        return result
    return wrapper
#
# @print_info
# def add_num(a, b):
#     return a + b
#
# r = add_num(10, 20)
# print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# r = add_num(10,20)
# print('start')
# print(r)
# print('end')

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args', args)
        print('kwargs', kwargs)
        result = func(*args, *kwargs)
        print('result', result)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

print("ラムダ####################################")
l = ['Mon', 'tue', 'Wed', 'Thu', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# sample_func = lambda word: word.capitalize()

# change_words( l, sample_func)

#ファンクションを引数に使う場合にはラムダを利用
change_words( l, lambda word: word.capitalize())
change_words( l, lambda word: word.lower())

print("ジェネレータ####################################")




