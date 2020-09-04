# Basic Practice:
# http://codingbat.com/python
#
# More Mathematical (and Harder) Practice:
# https://projecteuler.net/archives
#
# List of Practice Problems:
# http://www.codeabbey.com/index/task_list
#
# A SubReddit Devoted to Daily Practice Problems:
# https://www.reddit.com/r/dailyprogrammer
#
# A very tricky website with very few hints and touch problems (Not for beginners but still interesting)
# http://www.pythonchallenge.com/

myfile = open("myfile.txt")
print(myfile.read())
print(myfile.read()) #Trying to read file again won't return anything as the cursor is at the end of the file

print('*****************ResetTheCursor***************************')
#In order to reset the cursor
myfile.seek(0)
print(myfile.read())
print('****************************************************')

myfile.seek(0)
content = myfile.read()
print(content)
print('******************ReadLines()Method************************')

#Readlines function will return list of content in each line of the file
myfile.seek(0)
print(myfile.readlines())
myfile.close()
print('*************OpenFileFromAnyLocationInTheSystem*******************')

#Open files from different location from your system
myfile1 = open("DataStructureBasics/TestFiles/myfile1.txt")
print(myfile1.read())
myfile1.close()
print('***************OpenFileUsingWithKeyword***********************')

#Opening file using with
with open("DataStructureBasics/TestFiles/myfile1.txt") as my_new_file:
    contents = my_new_file.read()
    print(contents)

print('*********************OpeningFileInReadMode**********************')

with open("DataStructureBasics/TestFiles/myfile1.txt",mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)
print('*****************WritingToFile***********************************')

#Writing to file
with open("DataStructureBasics/TestFiles/myfile2.txt",mode='w') as f:
    f.write('I CREATED THIS FILE')

print('****************************************************')

with open("DataStructureBasics/TestFiles/myfile2.txt",mode='r') as r:
    print(r.read())

print('*****************AppendingToFile***********************************')

#Appending to a file
with open("DataStructureBasics/TestFiles/myfile1.txt",mode='a') as f:
    f.write('\nAppended the Fourth Line')

print('****************************************************')

with open("DataStructureBasics/TestFiles/myfile1.txt",mode='r') as r:
    print(r.read())