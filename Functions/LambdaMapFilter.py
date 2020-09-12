print('*****************Map**********************')

#map(func,*iterables) --> map object
#Make an iterator that computes the  function using arguments from each of the iterables.
#Stops when the shortest iterable is exhausted.

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

print('****************************************')

print(list(map(square,my_nums)))  #Returns the list

print('****************Map With Strings************************')

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally','Canada']

print(list(map(splicer,names)))

for item in map(splicer,names):
    print(item)

print('****************Filter************************')
#We need to filter by a function that returns either True or False

def check_even(num):
    return num%2 == 0  #Returns True for even numbers

mynums = [1,2,3,4,5,6]

for item in filter(check_even,mynums):  #Iterate over each item and print all items
    print(item)

print(list(filter(check_even,mynums)))  #List Output

print('****************Lambda************************')

#Normal function
def squarefunc(num):
    result = num ** 2
    return result

print(squarefunc(4))

print('*******************************************')

#Convert this function to lambda function

#def squarelambda(num): return num ** 2
squarefunc1 = lambda num: num** 2  #Lambda functions are anonymous and use lambda keyword
print(squarefunc1(5))              #def squarelambda from normal function is replaced by lambda

print('****************Lambda In Conjunction With Map************************')

mynums1 = [1,2,3,4,5,6]
print(list(map(lambda num: num** 2,mynums1)))

print('*******************************************')

for item in map(lambda num: num ** 2, mynums1):
    print(item)

print('****************Lambda In Conjunction With Filter************************')

print(list(filter(lambda num: num % 2 ==0,mynums1)))

print('*******************************************')

for item in filter(lambda num: num %2 == 0,mynums1):
    print(item)

print('*******************************************')
namelist = ['Andy','Eve','Sally','Canada']

#Grab first character of a list
print(list(map(lambda name:name[0],namelist)))

#Reverse the names in a list
print(list(map(lambda name:name[::-1],namelist)))