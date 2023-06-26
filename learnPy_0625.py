print("ファイル処理#############")
# f = open('test.txt', 'w')
# print('I am print', file=f)
# f.write('\n')
# f.write('testtest')
# f.write('\n')
# print('My', 'name','is', 'Mike',sep='#',end='!', file=f)
# f.write('\n')
# f.close()

# withステートメント　→　最終的にクローズまで行う。
# with open('test.txt', 'w') as f:
#     f.write('Test\n')

# 読み込み
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# with open('test.txt', 'w') as f:
#     f.write(s)

# 読み込み
# with open('test.txt', 'r') as  f:
#     # print(f.read())
#     while True:
#         chunk = 2
#         # line = f.readline()
#         line = f.read(chunk)
#         print(line)
#         # print(line, end='')
#         if not line:
#             break

print("seek#############")
# with open('test.txt', 'r') as  f:
#         print(f.tell())
#         print(f.read(1))
#         f.seek(5)
#         print(f.read(1))
#         f.seek(14)
#         print(f.read(1))
#         f.seek(15)
#         print(f.read(1))
#         f.seek(14)
#         print(f.read(1))

print("書き込みと読み込み#############")

# 書き込み　→　読み込みOK
# with open('test.txt', 'w+') as  f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# 読み込み　→　書き込みOK
# 最初に読み込めないとダメ!
# with open('test2.txt', 'r+') as  f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

print("テンプレート#############")
# $の変数に文字の代入が可能

import string

# s = """\
# Hi $name.
#
# $contents
#
# Have a good day
# """

# 別ファイルから読み込んでテキスト情報を利用

# with open('design/email_template.txt') as f:
#     t = string.Template(f.read())
#     contents = t.substitute(name='Mike', contents='How are you?')
#     print(contents)

print("CSV#############")
# import csv
#
# with open('test.csv', 'w') as csv_file:
#     fieldnames = ['Name', 'Count', 'Msg']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name':'A', 'Count':1,'Msg':'メッセージ'})
#     writer.writerow({'Name':'B', 'Count':2,'Msg':'メッセージ2'})
#
# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Count'])

print("ファイルの操作#############")
# import os

# 存在確認
# print(os.path.exists('test.txt'))
# # ファイルか否か確認
# print(os.path.isfile('test.txt'))
# # ディレクトリか否か確認
# print(os.path.isdir('test.txt'))
# print(os.path.isdir('design'))
# テキストファイルの名前変更
# os.rename('test.txt', 'rename.txt')
# リンクして、編集内容が反映される
# os.symlink('rename.txt', 'symlink.text')
# ディレクトリの作成
# os.mkdir('test_dir')
# ディレクトリの削除
# os.rmdir('test_dir')

import pathlib   #ファイル操作

# ファイルの作成
# pathlib.Path('empty.txt').touch()
# ファイルの削除
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))

import glob
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(glob.glob('test_dir/test_dir2/*'))

# import shutil
# # shutil.copy()
#
# shutil.rmtree('test_dir')
# print(os.getcwd())

print("tarfile#############")
# import os
# import tarfile
#
# directory = 'test_dir'
# if not os.path.exists(directory):
#     os.makedirs(directory)
#
#
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add(directory)
#
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     # tr.extractall(path='test_tar')
#     with tr.extractfile('test_dir/sub_dir/sub_text.txt') as f:
#         print(f.read())

print("zip file#############")
# import zipfile
# import glob
#
# with zipfile.ZipFile('test.zip', 'w') as z:
#     # z.write('test_dir')
#     # z.write('test_dir/test.txt')
#     for f in glob.glob('test_dir/**', recursive=True):
#         print(f)
#         z.write(f)
# with zipfile.ZipFile('test.zip', 'r') as z:
#     # z.extractall('zzz')
#     with z.open('test_dir/test.txt') as f:
#         print(f.read())

print("tempfile#############")
# import tempfile
#
# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())
#
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())
#
# with tempfile.TemporaryDirectory() as td:
#     print(td)
#
# temp_dir = tempfile.mkdtemp()
# print(temp_dir)

print("サブプロセス#############")
# OSコマンドをPython上で実行することができる
import subprocess

r = subprocess.run(['ls'])
subprocess.run(['ls', '-al'])

print("時間#############")
import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(now.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)

# 一年前の時間
d = datetime.timedelta(weeks=-1)
print(now + d)

# days=365
# weeks=1
# hours=1
# minute=1
# second=1
# microsecond=1

import time
# print("####")
# time.sleep(5)
# print("#")

print(time.time())

import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(file_name,now.now.strftime('%d/%m/%y')))

# with open(file_name, 'w') as f:
#     f.write('test')

# だめ
x = 1;
y = 2;

# 改行せよ（80まで）
x = 'aasadnsadjfndsnvndsfvnadvjnkajdnvkannvdsnckvnkkjdnvndkvnkdnfvkj nfdknv kjndfnvkfdnvjkndknvkjndfvkjndjkfvnkjndsvkjnvndv'

def test_funcp(x, y, z, fsdmfvmd,
              lvmds,lmfvsadmcmdsacvmdkvmpamvpamdvopmfdoivsjisjvoijsadiojijsdjmspdamjpsdmjmlvm='test'):
    print(1)

    """
    :param x:
    URLはOK
    See details at : http://dclknadsknvkldanvnadld.com/asdfpepovmdsnvksndfkvlnsdklnvklndsfklv/dafvjposjvposbmmgvpobmwbopmsprombvpoermwbmrbvopsmrvopmewopmv
    """
# 無駄な（）等はつけない
if (x and y):
    print('test')

# インデントは４つ
if x and y:
    print('test')

    x = {
        'test': 'sss'
    }

    x, y = y, x

# 関数やクラスごの改行は2行
def test_funcp(x, y, z, fsdmfvmd,
              lvmds,lmfvsadmcmdsacvmdkvmpamvpamdvopmfdoivsjisjvoijsadiojijsdjmspdamjpsdmjmlvm='test'):
    print(1)


def test_funcp(x, y, z, fsdmfvmd,
              lvmds,lmfvsadmcmdsacvmdkvmpamvpamdvopmfdoivsjisjvoijsadiojijsdjmspdamjpsdmjmlvm='test'):
    print(1)


long_word = []
for word in ['dsfsd', 'vnmkldmv', 'isdiocns']:
    long_word.append("{}dslcifjaslicj".format(word))
new_long_word = ''.join(long_word)

# まずはシングルクウォート
# ただし、シングルクウォートを入れる時にはダブルクウォート
# 文字を代入する際には特別にダブルクウォートにする

# TODO (tkita) Use locking mechanical

if x:
    print('exit')

if x: print('exit')

# クラスの場合はキャメルケース
# 関数名はスネークケース
# 変数名もスネークケース

# グローバル変数は大文字
# 書き換え禁止!!











