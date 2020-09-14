# Python comes with the built in debugger tool that allows you to interactively explore
# variables within mid-operation of our Python code

print('****************DEBUGGING USING PRINT STATEMENT************************')

x = [1,2,3]
y = 2
z = 3

result1 = y + z
#result2 = x + y #TypeError: can only concatenate list (not "int") to list

print(result1)
#print(result2)

print('****************DEBUGGING USING PYTHON DEBUGGER TRACE************************')

x = [1,2,3]
y = 2
z = 3

import pdb

result1 = y + z

#Set the trace before the error line
pdb.set_trace()
result2 = x + y