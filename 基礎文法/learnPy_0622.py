print("ジェネレータ####################################")
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)
print("#")
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)
print("#")

g = greeting()
print(next(g))
print("#")
print(next(g))
print("#")
print(next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'
c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("リスト内包表記####################################")

t = (1,2,3,4,5)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)

t2 = (5,6,7,8,9,10)

r = []
for j in t:
    r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]

print(r)

print("辞書内包表記####################################")
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)

d = {x: y for x, y in zip(w,f)}
print(d)

print("集合内包表記####################################")
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10) if i % 2}
print(s)

def g():
    for i in range(10):
        yield i

# g = g()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
g = g()
g = tuple(i for i in range(10) if i % 2 == 0)
print(type(g))
print(type(g))
print(type(g))
print(type(g))
print(g)
print(g)
print(g)
print(g)














