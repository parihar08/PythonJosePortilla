def myfunc(a,b):
    #Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))

print('***************************************')

'''When multiple arguments are required'''

#user can pass as many arguments as they want and it will be treated as tuple inside the function
def func(*args):
    return sum(args) *0.05

print(func(40,60,100))
print(func(40,60,100,200))
print(func(40,60,100,200,500,600))

print('***************************************')

def func1(*args):
    print(args)
func1(10,20,30)   #These arguments are treated as tuples inside the function

print('***************************************')

def fun(*args):
    for item in args:
        print(item) #Returns all items in args as a tuple

fun(10,20,30,40)
print('***************************************')
fun(50,60,70)

'''Keyword arguments'''
#user can pass as many arguments as they want and it will be treated as dictionary inside the function
print('***************************************')


def myfunc1(**kwargs):
    #print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc1(fruit='apple')
myfunc1(fruit='orange', veggie='lettuce')
myfunc1(veggie='lettuce')

print('***************************************')

def myfunc2(**kwargs):
    print(kwargs)

myfunc2(fruit='orange', veggie='lettuce') #Returns all items in kwargs as a dictionary

print('**************ArgsAndKwargsInCombination*******************')

'''args and kwargs in combination'''

def func2(*args,**kwargs):
    print(args) #Returns tuple
    print(kwargs) #Returns dictionary
    print('I would like {} {}'.format(args[0],kwargs['food']))

func2(10,20,30,fruit='orange',food='eggs',animal='dog')

print('***************************************')

def return_even(*args):
    #placeholder variable
    even_numbers =[]
    for num in args:
        if num%2==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(return_even(1,2,3,5,-2,4))

print('***************************************')

#Take string a input in a function and return uppercase even letter and lowercase odd letter

def test(str):
    list=[]
    for i in range(len(str)):
        if i%2==0:
            list.append(str[i].lower())
        else:
            list.append(str[i].upper())
    return ''.join(list)

print(test('sandeep parihar'))


