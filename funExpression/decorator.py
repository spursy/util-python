import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-03-25')
now()


def decoratorDemo3(text):
    def decoratorDemo2(func):
        @functools.wraps(func)
        def decoratorDemo3(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return decoratorDemo3
    return decoratorDemo2

@decoratorDemo3('execute')
def printNow():
    print('2016-06-06')

printNow()