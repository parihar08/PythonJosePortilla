def say_hello(name):
    print("Hello "+name)


def say_hello_default(name='Default'):
    print("Hello "+name)

say_hello('Sandeep')

say_hello_default()

def add_num(a,b):
    return a+b

result = add_num(2,3)
print(result)


def my_func(c,d):
    print(c+d)
    return c+d

my_func(5,6)


def sum_num(x,y):
    return x+y

print(sum_num(2,2.5))

print(sum_num('10','20')) #Any Data type can be passed at runtime