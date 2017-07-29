result = sorted([36,5,-12,9,21,-6])
print(result)

result1 = sorted([36,5,-12,9,21,-6], key = abs)
print(result1)

result2 = sorted(['bob', 'asasd', 'ASS', 'WSXZZ'], key = str.lower)
print(result2)

result3 = sorted(['bob', 'asasd', 'ASS', 'WSXZZ'], key = str.lower, reverse = True)
print(result3)


