import math

#help(math)
print('***************MATH MODULE*************************')

value = 4.35
print(math.floor(value))    #4
print(math.ceil(value))     #5
print(round(value))         #4
print(round(5.5))           #6
print(round(4.5))           #4 - Round goes towards the even number

print('****************************************')

print(math.pi)  #3.141592653589793

from math import pi
print(pi)       #3.141592653589793

print('****************************************')

print(math.e)   #2.718281828459045
print(math.inf) #Infinity
print(math.nan) #Not a number

#Numpy library specifically designed for Numerical processing

print('****************************************')

print(math.log(math.e))     #1.0

print(math.log(100,10))     #2 --> 10^2 = 100

print('****************************************')

print(math.sin(10))
print(math.degrees(pi/2))   #90 degree
print(math.radians(180))    #3.14 (pi)

print('***************RANDOM MODULE*************************')

import random

print(random.randint(0,100))

print('****************************************')

#What if we want to test on same batch of random numbers. Here, SEED comes into play
#This means same random numbers will show up in a series

random.seed(101)
print(random.randint(0,100))    #74
print(random.randint(0,100))    #24
print(random.randint(0,100))    #69
print(random.randint(0,100))    #45
print(random.randint(0,100))    #59

print('****************************************')

random.seed(42)
print(random.randint(0,41))
print(random.randint(0,41))
print(random.randint(0,41))
print(random.randint(0,41))
print(random.randint(0,41))

print('****************************************')

mylist = list(range(0,20))
print(mylist)
#Choose a random number from the list
print(random.choice(mylist))

#Grab 5 random numbers from the list
print('**********SAMPLING WITH REPLACEMENT******************************')

#1. Sampling with replacement - Allowing ourselves to pick same number twice
print(random.choices(population=mylist,k=10))
print('\n')

print('**********SAMPLING WITHOUT REPLACEMENT******************************')

#2. Sampling without replacement - Can't pick same number twice
print(random.sample(population=mylist,k=10))
print('\n')

print('**************SHUFFLING A LIST**************************')
print(mylist)
print('\n')
random.shuffle(mylist) #Permanently affects the list
print(mylist)
print('\n')

print('**************PROBABILITY DISTRIBUTION**************************')

#.1 Uniform Distribution
print('\n')
print(random.uniform(a=0,b=100)) #Will pick a number between 0-100 up to very high precision

#.2 Normal/Gauss Distribution
print('\n')
print(random.gauss(mu=0,sigma=1)) #mu -mean   sigma- standard deviation