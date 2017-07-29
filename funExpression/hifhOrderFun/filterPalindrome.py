# -*- coding: utf-8 -*-

# print(list(range(1, 1000)))

def getPalindrome(n):
    if str(n)==str(n)[::-1]:
        return n

result = filter(getPalindrome, list(range(1, 1000)))
print(list(result))