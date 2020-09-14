#1. Create a generator that generates squares of number up to some number n

def gen_squares(n):
    for x in range(n):
        yield x**2

for x in gen_squares(10):
    print(x)

print('****************************************')
#2. Create a generator that yields 'n' random numbers between low and high numbers(that are input)
#Note use random library

import random

def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,8):
    print(num)

print('****************************************')
#3. Use a iter() function to convert below string into iterator

s = 'hello'

s_iter = iter(s)
print(next(s_iter)) #h
print(next(s_iter)) #e
print(next(s_iter)) #l
print(next(s_iter)) #l
print(next(s_iter)) #o
#print(next(s_iter)) #StopIteration - Error as we have already yielded all the values

print('****************************************')
#5. Example of use case of generator with a yield statement where we do not want to use
#normal function with a return statement

#If the Output has the potential of taking up large amount of memory and you only intend to
#iterate through, you would want to use a generator

print('****************************************')
#6. Explain what gencomp is in the code below?

#Hint Generator Comprehension!

#Generator comprehension will hold (item for item in my_list if item >3) in memory
#List comprehension has [] -square brackets and Generator comprehension has () - parenthesis

my_list = [1,2,3,4,5]

gen_comp = (item for item in my_list if item >3)

for item in gen_comp:
    print(item)

