#Immutability - Cannot change

name = 'Sam'
#name[0] = 'P'  #Cannot do this - TypeError: 'str' object does not support item assignment
#print(name)
print('************************************')

#String Concatenation
name1 = 'Sam'
last_letters = name1[1:]
print(last_letters)
print('P' + last_letters)

print('************************************')

x = 'Hello World'
print(x + " it is beautiful outside")

print('************************************')

letter = 'z'
print(letter*10)
print('************************************')

#Cannot concatenate letters with a string
str1 ='2'
str2 = '3'
print(str1+str2)  #Output would be 23 instead of 5
print('************************************')

#String methods
a = 'Hello World'
print(a.upper())
print(a.lower())
print(a.split())  #Split the string based on white space or the letter we passed on
print(a.split('l')) #Split returns the list on based on letter l
print('************************************')
