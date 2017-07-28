L = []
n = 1
while n < 20:
    L.append(n)
    n = n + 2

print(L)

for i in L:
    print(i)

print('      ')

for ch in "asadsfsdf":
    print(ch)

print('      ') 

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

from collections import Iterable
print(isinstance('abc', Iterable))

for x,y in [(1,2), (3,4), (5,6)]:
    print(x, y)
