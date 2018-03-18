# From: https://www.programiz.com/python-programming/decorator
def first(msg):
    print(msg)
first('hello')
second = first
second('hello')

# higher order funcitons
def inc(x):
    return x + 1
def dec(x):
    return x - 1
def operate(func, x):
    result = func(x)
    return result 
print(operate(inc, 3))
print(operate(dec, 3))

# A function can return another function 
def is_called():
    def is_returned():
        print('hello')
    return is_returned 
new = is_called()
new()

# A decorator is a callable that returns a callable
# It takes a functino, adds some functionality and returns it
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
# ordinary = make_pretty(ordinary)
# ordinary()
# equals to -->
@make_pretty
def ordinary():
    print("I'm ordinary")
ordinary()

# An example of using a decorator to check if a number is divide by zero
def smart_divide(func):
    def inner(a,b):
        print("I'm gonna divide", a, "and", b)
        if b == 0:
            print("Whoops! Can't divide")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    return a/b
print(divide(2,0))


    