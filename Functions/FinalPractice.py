#Write a function that computes volume of sphere given its radius

def vol(rad):
    return ((4/3)*(3.14)*(rad**3))

print(vol(2))

print('****************************************')

#Write a function that checks whether a number is in a given range(inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range between {low} and {high}')
    else:
        print(f'{num} is not in range between {low} and {high}')

ran_check(5,2,7)
ran_check(7,2,5)
ran_check(7,2,7)
ran_check(2,2,7)

print('****************************************')

def ran_bool(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

print(ran_bool(5,2,7))
print(ran_bool(7,2,5))
print(ran_bool(7,2,7))
print(ran_bool(2,2,7))

print('****************************************')

#Write a function that accepts a string and calculates number of upper case and lower case letters
# str = 'Test String'
# for i in str:
#     print(i)
#     print(i.isupper())

#Using List
def up_low(mystring):
    upper_list = []
    lower_list = []
    for i in mystring:
        if i.isupper():
            upper_list.append(i)
        elif i.islower():
            lower_list.append(i)
    print('Original String: ', mystring)
    print('No. of Upper case characters: ',len(upper_list))
    print('No. of Lower case characters: ',len(lower_list))

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

print('****************************************')
#Using simple counter
def up_low1(mystring):
    upper = 0
    lower = 0
    for i in mystring:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else :
            pass
    print('Original String: ', mystring)
    print('No. of Upper case characters: ',upper)
    print('No. of Lower case characters: ',lower)

up_low1('Hello Mr. Rogers, how are you this fine Tuesday?')

print('****************************************')
#Using Dictionary
def up_low1(mystring):
    dict = {'upper':0, 'lower':0}
    for i in mystring:
        if i.isupper():
            dict['upper'] += 1
        elif i.islower():
            dict['lower'] += 1
        else :
            pass
    print('Original String: ', mystring)
    print('No. of Upper case characters: ',dict['upper'])
    print('No. of Lower case characters: ',dict['lower'])

up_low1('Hello Mr. Rogers, how are you this fine Tuesday?')

print('****************************************')

#Write a function that takes a list and returns a new list with the unique elements of first list
# samplelist = [1,1,1,2,2,2,3,3,3,4,4,5,5,5]
# uniquelist = [1,2,3,4,5]

def unique_list(lst):
    uniqueset =set(lst)
    return list(uniqueset)

samplelist = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,8,8,8,1]
print(unique_list(samplelist))

print('****************************************')

def unique_list1(lst):
    seen_numbers = []
    for num in lst:
        if num not in seen_numbers:
            seen_numbers.append(num)
    return seen_numbers

samplelist = [1,1,1,4,4,5,5,5,6,8,8,8,1]
print(unique_list1(samplelist))

print('****************************************')

#Write a function to multiply all numbers in a list:
def multiply(numbers):
    total = 1
    for num in numbers:
        total = total*num
    return total

numlist = [1,2,3,4,5,-2]
print(multiply(numlist))

print('****************************************')

#Write a function to check whether a word or a string is palindrome or now

def palindrome(str):
    #Remove the spaces in a string
    str = str.replace(' ', '')
    rev_str = str[::-1]
    if rev_str == str:
        return True
    else:
        return False

print(palindrome('madam'))
print(palindrome('kayak'))
print(palindrome('racecar'))
print(palindrome('nurses run'))
print(palindrome('test'))

print('****************************************')

#Write a function to check whether a string is pangram or not
#Pangram are words or sentences containing every letter of alphabet at least once

import string

def is_pangram(str1,alphabet=string.ascii_lowercase):
    for i in alphabet:
        if i in str1:
            return True
        else:
            return False

print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('The quick brown fox jumps'))
print(is_pangram('Test string'))
print(is_pangram(string.ascii_lowercase))

print('****************************************')

def is_pangram1(str1,alphabet=string.ascii_lowercase):
    #Create a set of alphabets
    alphaset = set(alphabet)
    #Remove any spaces from input string
    str1 = str1.replace(' ','')
    #Convert all into lowercase
    str1 = str1.lower()
    #Grab all unique letters from the string set()
    str1 = set(str1)
    #Compare alphabet set with string set input
    return str1 == alphaset

print(is_pangram1('The quick brown fox jumps over the lazy dog'))
print(is_pangram1('The quick brown fox jumps'))
print(is_pangram1('Test string'))
print(is_pangram1(string.ascii_lowercase))