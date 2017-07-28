g = (x * x for x in list(range(1, 11)))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


for n in g:
    print(n)

print('                      ')

def fib(max):
    n, a, b = 0,0,1
    while n < max:
        yield b
        a,b = b, a + b
        n = n + 1
    return 'done'

print(fib(5))

print('                      ')

for data in fib(6):
    print(data)



gen = fib(7)
while True:
    try: 
        x = next(gen)
        print('the value is ', x)
    except StopIteration as e:
        print('Generator return value is ', e.value)
        break



