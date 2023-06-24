print("名前空間スコープ####################################")

# ok
animal = 'cat'
print(animal)

# ok
def f():
    print(animal)
f()

# ng
# def f():
#     print(animal)
#     animal = 'dog'
# f()

#  ok
def f():
#     print(animal)
    animal = 'dog'
    print(animal)
    print(locals())
f()

# dogにはならない
print('global:', animal)

# dogになった
def f():
    global animal
    animal = 'dog'
    print(animal)
f()

print('global:', animal)
print(globals())

animal = 'cat'

def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print('global',__name__)

print("例外処理####################################")
# 例外を発生してプログラムが終了しない
l = [1,2,3]
i = 5

try:
    l[i]
except:
    print("Don't worry")

print("end")

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))

print("end")

del l

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)

print("last")

i = 0

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other: {}".format(ex))
#成功した場合のみエラーなく抜けた場合
else:
    print('done')
finally:
    print('clean up')

print("last")

print("独自　例外処理####################################")
# raise IndexError('test error')
#
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    # words = ['apple', 'orange', 'banana']
    for word in words:
        # 条件に引っかかった場合にエラー
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault.Go next')











