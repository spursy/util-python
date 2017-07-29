# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1

result = list(filter(is_odd, [1,2,3,4,5,6,7]))
print(result)

# filter null or empty
def not_empty(s):
    return s and s.strip()

result2 = list(filter(not_empty, ['A', '', 'B', None, 'C']))
print(result2)

# calculate prime numbers
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x %n > 0

def primes() :
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if (n < 1000):
        print(n)
    else: 
        break
