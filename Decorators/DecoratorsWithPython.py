#Decorators allow us to decorate a function

#Add some new capability to the function

# def simple_func():
#     #Want to do more stuff!
#     #Do simple stuff
#     return something

#There are 2 options:
#1. Add that extra code(functionality) to your old function
#2. Create a brand new function that contains the old code, and then add new code to it

#Now what if we want to remove that extra functionality. We have to do it manually
#Is there a better way ? May be an on/off switch to quickly add this functionality

#PYTHON HAS DECORATORS THAT ALLOWS US TO TACK ON EXTRA FUNCTIONALITY TO AN ALREADY EXISTING
#FUNCTION. THEY USE @operator AND ARE THEN PLACED ON THE TOP OF THE ORIGINAL FUNCTION

#Manually building a decorator

def func():
    return 1

print(func())
print(func)  #This means we can assign functions to another variable and execute them off those variables

print('****************************************')

def hello():
    return "Hello!"

print(hello())
print(hello)

greet = hello #Assigning functions to another variable
print(greet()) #Executing function off another variable to which it was assigned

del hello  #Even though we deleted the name hello

print(greet()) #This prints Hello!. The name greet is actually pointing to that original function hello object

#print(hello()) #Gives NameError name hello is not defined

#FUNCTIONS ARE OBJECTS THAT CAN BE PASSED INTO OTHER OBJECTS

print('*********PASSING FUNCTION WITHIN ANOTHER FUNCTION**************')

def hello(name='Jose'):
    print('The hello() function has been executed!')

    #The scope of the greet() and welcome() function is only inside the hello() function
    def greet():
        return '\t This is the greet() function inside hello()'

    def welcome():
        return '\t This is the welcome() function inside hello()'

    print(greet())
    print(welcome())
    print('This is the end of the hello() function')

hello()

print('*********How to access greet() and welcome() fn outside of hello()*********')
#We can do is hello() function return a function

def hello(name='Jose'):
    print('The hello() function has been executed!')

    #The scope of the greet() and welcome() function is only inside the hello() function
    def greet():
        return '\t This is the greet() function inside hello()'

    def welcome():
        return '\t This is the welcome() function inside hello()'

    print("I'm going to return a function")

    if name == 'Jose':
        return greet

    else:
        return welcome

#Assigning functions to another variable
my_new_func= hello('Jose')
my_new_func()
print('****************************************')
print(my_new_func)

print('****************************************')
#Executing function off another variable to which it was assigned
print(my_new_func()) #Return function within a function

print('****************************************')

#Assigning functions to another variable
my_new_func1= hello('Sandeep')
my_new_func1()
print('****************************************')
print(my_new_func1)

print('****************************************')
#Executing function off another variable to which it was assigned
print(my_new_func1())  #Return function within a function

print('*************RETURN FUNCTION WITHIN A FUNCTION****************')

def cool():

    def super_cool():
        return "I'm very cool!"

    return super_cool

some_func = cool()
print(some_func())

print('****************************************')

def cool():

    def super_cool():
        return "I'm very cool!"

    return super_cool()

some_func = cool()
print(some_func)

print('*************PASSING A FUNCTION AS AN ARGUMENT****************')

def hello():
    return "Hi Jose!"

def other(some_def_func): #Pass in a function in to other function
    print('Other code runs here!') #Do some stuff
    print(some_def_func()) #Execute the function

print(hello)
print('****************************************')
other(hello)

print('***************CREATE A DECORATOR*************************')

def new_decorator(original_func):

    def wrap_func(): #This is the extra functionality that want to wrap original function with
        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()
print('****************************************')
#Assigning functions to another variable
decorated_func = new_decorator(func_needs_decorator)
#Executing function off another variable to which it was assigned
decorated_func()

print('****************************************')

#There is a special syntax for this line: decorated_func = new_decorator(func_needs_decorator)

#Turn On Decorator
@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()

print('****************************************')

#Turn Off Decorator

#@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()


