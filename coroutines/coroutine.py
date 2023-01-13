def func():
    print("part 1")

    yield

    print("part 2")

    yield 

    print("part 3")

try:
    y = func()

    next(y)
    next(y)
    next(y)
    
except:
    pass

#REFERENCE: https://betterprogramming.pub/coroutines-in-python-building-blocks-of-asynchronous-programming-40c39d9ed420