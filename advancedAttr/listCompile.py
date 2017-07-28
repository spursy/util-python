L = list(range(1,11))
# 1,2,3,4,5,6,7,8,9,10
print(L)

L1 = []
for x in range(1, 11):
    L1.append(x * x)
# 1,4,9,16,25,36,49,64  ,,,,,,,,
print(L1)

# 1,4,9,16,25,36,49,64  ,,,,,,,,
L2 = [x * x for x in range(1, 10)]
print(L2)

#4, 16, 36, 64
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)

L4 = [m + n for m in "ABC" for n in "121345"]
print(L4)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L5 = [k + '=' + v for k, v in d.items()]
print(L5)
