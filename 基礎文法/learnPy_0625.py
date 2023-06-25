print("クラスの初期化####################################")

# class Person(object):
#
#     # __init__インスタンス化時に呼び出される関数　→　コンストラクタ
#     def __init__(self, name):
#         self.name = name
#         print('first', self.name)
#
#     def say_something(self):
#         # self.nameは他のメソッドからでもアクセス可能
#         print('I am {}. hello'.format(self.name))
#         self.run(10)
#
#     def run(self, num):
#         print('run' * num)
#
#     # __del__クラス内容の実行終了時に最後に呼び出される関数　→　デストラクタ
#     # オブジェクトが使われなくなった時点で発動
#     def __del__(self):
#         print('good bye')
#
# person = Person('Mike')
# person.say_something()
#
# print('#区切り#')
#
# del person

print("クラスの継承####################################")
# class Car(object):
#     def run(self):
#         print('run')
#     pass
#
# class ToyotaCar(Car):
#     pass
#
# class TeslaCar(Car):
#     def auto_run(self):
#         print('auto_run')

# print('##Car##')
# car = Car()
# car.run()
# print('##ToyotaCar##　→　Carの機能を継承')
# toyota_car = ToyotaCar()
# toyota_car.run()
# print('##TeslaCar##　→　Carの機能を継承 + 独自の機能を持ち合わせている')
# tesla_car = TeslaCar()
# tesla_car.auto_run()
# tesla_car.run()

print("クラスのオーバーライド####################################")
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')
#     pass
#
# class ToyotaCar(Car):
#     pass
#
# class TeslaCar(Car):
#     def __init__(self, model='Model s', enable_auto_run=False, passwd='123'):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
#         self.passwd = passwd
#
#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
#
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == '456':
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError
#
#     def run(self):
#         print('super fast!')
#
#     def auto_run(self):
#         print('auto_run')
#
#
# print('##Car##')
# car = Car()
# car.run()
# print('##ToyotaCar##　→　Carの機能を継承')
# toyota_car = ToyotaCar('Lexus')
# toyota_car.run()
#
# print(toyota_car.model)
# print('##TeslaCar##　→　Carの機能を継承 + 独自の機能を持ち合わせている')
# tesla_car = TeslaCar('Model s', passwd='111')
# # tesla_car = TeslaCar()
# # tesla_car.auto_run()
# tesla_car.run()
#
# print(tesla_car.model)
# # print(tesla_car.enable_auto_run)
# # tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)
#
# class T(object):
#     pass
#
# t = T()
# t.name = 'Mike'
# t.age = 20
# print(t.name, t.age)

# class Person(object):
#     def __init__(self, age=1):
#         self.age = age
#     def drive(self):
#         if self.age >= 18:
#             print('ok')
#         else:
#             raise Exception('No drive')
#
# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# baby = Baby()
# adult = Adult()
#
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')
#     def ride(self, person):
#         person.drive()
#     pass
#
# car = Car()
# car.ride(adult)

print("多重継承####################################")
# class Person(object):
#     def talk(self):
#         print('talk')
#     def run(self):
#         print('person of run')
#
# class Car(object):
#     def run(self):
#         print('run')
#
# #                      ↓順番によって呼び出す順番も変わってくる
# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print('fly')
#
# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()

print("クラス変数####################################")

# class Person(object):
#
#     # クラス変数
#     kind = 'human'
#
#     def __init__(self, name):
#         # self.kind = 'human'
#         self.name = name
#
#     def who_are_you(self):
#         print(self.name, self.kind)
#
# a = Person('A')
# a.who_are_you()
#
# a = Person('B')
# a.who_are_you()
#
# class T(object):
#
#     # words = []
#
#     def __init__(self):
#         self.words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
# c = T()
# c.add_word('Add 1')
# c.add_word('Add 2')
# print(c.words)
#
# d = T()
# d.add_word('Add 3')
# d.add_word('Add 4')
#
# # リストは共有される
# print(c.words)


print("クラスメソッド / スタティックメソッド####################################")

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.x)
print(a.kind)
b = Person
# print(b.x)    エラー
print(b)
print(b.kind)

Person.about(1999)


print("特殊メソッド####################################")

class Word(object):

    def __init__(self, text):
        self.text = text

    # 文字列として呼ばれた時に読み込まれる
    def __str__(self):
        return 'Word!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('######')
print(len(w))

print(w == w2)







