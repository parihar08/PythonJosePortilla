#Generator functions allow us to write a function that can send back a value and then later
#resume to pickup from where it left off.
# This allows us to generate a sequence of values overtime

#The main difference in the syntax will be the use of YIELD statement

#When a generator function is complied they become an object that supports an iteration protocol
#That means when they can called in our code they do not actually return a value and then exit

#Generator functions will automatically suspend and resume their execution and state around
#the last point of value generation

#The advantage is that instead of having to compute an entire series of values upfront,
#the generator computes one value and waits until the next value is called for.

#For example, the range() function doesn't produce a list in memory for all the values from
#start to stop. Instead it just keeps track of the last number and the step size, to provide
#a flow of numbers.
print('****************************************')

#Working with normal function. We are keeping this entire result list in memory
def create_cubes(n):
    result = []
    for x in range(0,n):
        result.append(x**3)
    return result

print('****************************************')

print(create_cubes(10))

for x in create_cubes(10):
    print(x)

print('****************************************')
#We only need one value at a time to print the cubes. We don't need entire list in the memory
#We just need the previous value and the formula to get to the next value in order to generate
#all these cubes. Instead of creating this giant list in memory, it would be better if we
#could yield the actual cubed numbers

def create_cubes(n):
    for x in range(n):
        yield x**3

#We no longer see the list when we print create_cubes. We have to iterate through it to get
#the list of numbers
print(create_cubes(10)) #<generator object create_cubes at 0x7fa864a703c0>

print('****************************************')

for x in create_cubes(10):
    print(x)  #We get back the same result as before.Now it doesn't need to create list in memory

print('****************************************')

#If we do want to get it in list, we can cast it into list and get the list
print(list(create_cubes(10)))

print('***************CALCULATE FIBONACCI SEQUENCE*************************')

#Without yield - Way less memory efficient as we are holding everything in a list.
def gen_fibonacci(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

for num in gen_fibonacci(10):
    print(num)

print('****************************************')

#With yield - Memory efficient as we are yielding numbers as we need them.
def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in gen_fibonacci(10):
    print(num)

print('***************NEXT AND ITER FUNCTIONS*************************')

def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

print('****************************************')

g = simple_gen() #g is new instance of simple_gen() function
print(g)  #<generator object simple_gen at 0x7fc3cb870580>

print('****************************************')
#Generator objects just need the previous value and the formula to get to the next value
#in order to generate all the values. Its not holding everything in memory
print(next(g)) #0
print(next(g)) #1
print(next(g)) #2
#print(next(g)) #StopIteration - Error as we have already yielded all the values

print('*****************ITER***********************')

s = 'hello'
for letter in s:
    print(letter)

print('****************************************')

#next(s) #TypeError: 'str' object is not an iterator

#We cannot directly iterate over string object using next function just like we did on
#generator. In order to turn String into a Generator, we need iterator function

s_iter = iter(s)
print(next(s_iter)) #h
print(next(s_iter)) #e
print(next(s_iter)) #l
print(next(s_iter)) #l
print(next(s_iter)) #o
#print(next(s_iter)) #StopIteration - Error as we have already yielded all the values

print('***************CREATE A GENERATOR*************************')


