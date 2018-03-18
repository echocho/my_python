def startAt(x):
    def incrementBy(y):
        return x+y
    return incrementBy
a = startAt(1)
print('funciton:', a)
print('result:', a(3))
print('type of a(1):', type(a(1)))
print('type of a:', type(a))

# 闭包无法修改外部函数的局部变量
def outerFunc():
    x = 0
    def innerFunc():
        x = 1
        print('inner x:', x==1)
    print('outer x before calling inner:', x==0)
    innerFunc()
    print('outer x after calling inner:', x==0)
outerFunc()

# python循环中不包含域的概念
flist = []
for i in range(3):
    print('outer loop, i=', i)
    def func(x):
        print('inner loop, x=', x)
        return x * i
    flist.append(func)
    print('flist = ', flist)
for f in flist:
    print('another loop, f=', f)
    print(f(2))

# 修改方案
flist = []
for i in range(3):
    def makefunc(i):
        def func(x):
            return x * i 
        return func
    flist.append(makefunc(i))
for f in flist:
    print(f(2))


# Nested function
def print_msg(msg):
    def printer():
        print(msg)
    printer()
print_msg('Hello')

# # Define closure
def print_msg(msg):
    def printer():
        print(msg)
    return printer
another = print_msg('Hello')
another()

# An example where a closure might be more preferable than defining a class and making objects
def make_multiplier_of(n):
    print('outer n=', n)
    def multiplier(x):
        print('x=', x)
        print('n=', n)
        return x * n 
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))