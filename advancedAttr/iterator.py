# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

from collections import Iterator

print(isinstance([] , Iterator))

print(isinstance((x for x in range(1, 11)) , Iterator))


it = iter([1,3,5,7,9,11])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("End")
        break 