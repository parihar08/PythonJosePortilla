x = 25
def printer():
    x = 50
    return x

print(x)  #25
print(printer())  #50

print('*******************************************')

#Scope of Variables: LEGB Rule
# L: Local
# E: Enclosing function locals
# G: Global(module)
# B: Built-in(Python)

#Here num is local
print(list(map(lambda num: num ** 2,[1,2,3])))

print('*******************************************')

#Enclosing function locals - name used in hello function is local to enclosing function greet
name = 'THIS IS A GLOBAL STRING'
def greet():
    name = 'Sammy'
    def hello():
        print('Hello '+name)

    hello()

greet()

print('*******************************************')

#Global - here name is found in the global namespace
name1 = 'THIS IS A GLOBAL STRING'
def greet1():
    def hello1():
        print('Hello '+name1)

    hello1()

greet1()

print('*******************************************')

a = 50
def func(a):
    print(f'A is {a}')

    #Local Reassignment
    a = 200
    print(f'I JUST LOCALLY CHANGED A TO {a}')

func(a) # 50, 200
print('*******************************************')
print(a) #50

print('*******************************************')
#If we want to change the value of global b
b = 50
def func():
    global b
    print(f'B is {b}')

    #Local Reassignment
    b = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL B TO {b}')

func() # 50, NEW VALUE
print('*******************************************')
print(b) #NEW VALUE

print('*******************************************')
#If we want to change the value of global c without using global keyword
c = 50
def func(c):
    print(f'C is {c}')

    #Local Reassignment
    c = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED C TO {c}')
    return c

c = func(c) # 50, NEW VALUE
print('*******************************************')
print(c) #NEW VALUE