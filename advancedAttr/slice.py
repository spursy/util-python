L = []
n = 1;
while n < 20:
    L.append(n)
    n = n + 2

# 1,3,5,7,9,11,13,15,17,19
print(L)   

#1,3,5
print(L[0:3])

#1,3,5
print(L[:3])

#17,19
print(L[-2:])

# 1,5,9,13
print(L[:8:2])

#1,5,9,13,17
print(L[::2])

# 1,3,5,7,9,11,13,15,17,19
print(L[:])