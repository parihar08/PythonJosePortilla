# Time your code's performance
# 3 main ways of doing this:
# 1. Simply tracking time elapsed
# 2. Using the timeit module
# 3. Special %%timeit 'magic' for Jupyter notebooks

print('*****************TRACKING TIME ELAPSED*********************','\n')

import time

def func1(n):
    return [str(num) for num in range(n)] #Using List Comprehension

#Current Time Before
start_time = time.time()
#Run the Code
result = func1(1000000)
#Current Time After
end_time = time.time()
#Elapsed Time
elapsed_time = end_time - start_time
print('func()1 time: ',elapsed_time)

print('**************************************************')

def func2(n):
    return list(map(str,range(n)))        #Using Map
#Current Time Before
start_time = time.time()
#Run the Code
result1 = func2(1000000)
#Current Time After Running Code
end_time = time.time()
#Elapsed Time
elapsed_time = end_time - start_time
print('func()2 time: ',elapsed_time)

#Here using time tracking, precision may not be enough for pieces of code which run very fast.
#That's why we have Timeit Module which tracks very high precision of code which run very fast.

print('*******************TIMEIT MODULE*******************','\n')
#Timeit will run set of statement code over and over again as per the number defined

import timeit

#Statement and setup are passed in as Strings
#Statement is the actual code which we want to run
stmt1 = '''
func1(100)      
'''

#Setup is the code which we need to call statement over and over again
#Statement is calling func1() -->Hence, setup should have func1() defined
setup1 = '''
def func1(n):
    return [str(num) for num in range(n)]
'''
print('func()1 time: ',timeit.timeit(stmt=stmt1,setup=setup1,number=100000))

print('**************************************************')

stmt2 = '''
func2(100)
'''

setup2 = '''
def func2(n):
    return list(map(str,range(n)))  
'''

print('func()2 time: ',timeit.timeit(stmt=stmt2,setup=setup2,number=100000))