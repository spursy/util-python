def int2(x, base = 2):
    return int(x, base)

result = int2('10101010')
print(result)


# functools.partial help me create partial function.
import functools
int02 = functools.partial(int, base = 8)
result2 = int02('1111')
print(result2)