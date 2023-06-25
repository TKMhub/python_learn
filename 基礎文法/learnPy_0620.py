print("ディクショナリー型####################################")
# fruits = {
#     'apple':100,
#     'banana':200,
#     'orange':300
# }
# print(fruits['apple'])
print("集合型####################################")
# a = {1,2,2,2,5,6,7,8,2}
# b = {1,2}
# print(a)
# print(a-b)
# print(a&b)
# a.add(6)
# print(a)
# a.add(6)
# print(a)
# a.remove(6)
# print(a)
# #引数なし
# a.clear()
# print(a)
#
# my_friends = {'a', 'b', 'c'}
# a_friends = {'c','g'}
# print(my_friends & a_friends)
#
# # リスト→集合に型変換をしてユニークなものを取得
# #リスト
# my_friends = ['a', 'a', 'c']
# #集合へ変換
# unique_friends = set(my_friends)
# print(my_friends)
# print(unique_friends)

"""
複数行のコメントアウト

テスト
テスト
テスト 
"""
# OK
# s = 'aaaaaa'+'bbbbbb'
# OK（バックスラッシュ）→ 80文字で次の行に行くべきである
# s = 'aaaaaa'\
#     +'bbbbbb'
#OK
# s = ('aaaaaa'
#     +'bbbbbb')

print("if文####################################")
# x = 0
# y = 2
#
# if x < 10:
#     print('negative')
#     if y < 3:
#         print('インデントを合わせてね')
# elif x == 0:
#     print('x=0')
# else:
#     print('non')
print("in/not####################################")
# y = [1,2,3]
# x = 1
# if x in y:
#     print('in')
#
# y = [1,2,3]
# x = 5
# if x not in y:
#     print('not in')
#
# a = 1
# b = 2
# if not a == b:
#     print('not equal')
# if a != b:
#     print('not equal')
# if a > b:
#     print('not equal')
#
# is_ok = True
# if is_ok:
#     print(True)
# if not is_ok:
#     print(True)
# else:
#     print('not')

"""
値や文字が入っている → True
0や0.0、''空 → False
"""
# is_ok = 1
# if is_ok:
#     print('ok')
# else:
#     print('ng')
#
# is_ok = 0
# if is_ok:
#     print('ok')
# else:
#     print('ng')
#
# is_ok = 'ok?'
# if is_ok:
#     print('ok')
# else:
#     print('ng')
#
# is_ok = ''
# if is_ok:
#     print('ok')
# else:
#     print('ng')
#
# is_empty = None
# print(type(is_empty))
# if is_empty is None:
#     print('None')
# if is_empty is not None:
#     print('not None')
# else:
#     print('None')

print("while####################################")
# const = 0
# while const < 5:
#     print(const)
#     const += 1
# count2 = 0
# while True:
#     print(count2)
#     if count2 >= 5:
#         break
#     count2 += 1
#
# count2 = 0
# while True:
#     if count2 >= 5:
#         break
#     if count2 == 2:
#         continue
#     print(count2)
#     count2 += 1
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('Done')

# 対話式でユーザーの入力 → input
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')
print("for文####################################")
# some_list = [1,2,3,4,5]
#
# for i in some_list:
#     print(i)
#
# for s in 'abcde':
#     print(s)
#
# for word in ['My', 'Name', 'is', 'tkm']:
#     # if word == 'is':
#     #     break
#     if word == 'Name':
#         continue
#     print(word)
# else:
#     # breakで終了すると、elseは実行されない。
#     print('end : for else')
# 10回ハローと出力する
for i in range(10):
    print('Hello')
for i in range(3, 10, 2):
    print(i)
# i不要（インデックス使わず）
for _ in range(10):
    print('Hello2')

for i, fruit in enumerate(['app', 'banana', 'oren']):
    print(i+1, fruit)


































