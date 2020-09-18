#Range is a generator function- special type of function which generates information instead of saving to memory
print('***************Range*******************')
for num in range(4):
    print(num)

for num in range(3,8):
    print(num)

for num in range(0,11,2):
    print(num)

print('***************Enumerate*******************')
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1

print('*******************************************')
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

print('*******************************************')
word = 'abcde'
for item in enumerate(word):
    print(item)  #It returns tuples with index and their values

print('*******************************************')
word = 'abcde'
for index,letter in enumerate(word):
    print(index)  #Use tuples unpacking technique to get index and respective value
    print(letter)
    print('\n')

print('******************Zip*************************')
#Zip function is opposite of enumerate and zips together two lists
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

zip(list1,list2) #Returns nothing

for item in zip(list1,list2):
    print(item)  #Returns list of tuples - (1,'a') (2,'b') ......

print('**********************************************')

list3 = [100,200,300,400,500]
for item in zip(list1,list2,list3):
    print(item)  #Returns list of tuples - (1,'a',100) (2,'b',200) ......

print('**********************************************')

#What happens if the lists are uneven?
#Zip will only take into account as far as elements are even in all lists
list1 = [1,2,3,4,5,6,7,8,9]
list2 = ['a','b','c','d']
list3 = [100,200,300,400,500,600]

for item in zip(list1,list2,list3):
    print(item)  #Returns only 4 records in list of tuples as list2 has max 4 elements
                 #(1,'a',100) (2,'b',200) (3,'c',300) (4,'d',400)

print('**********************************************')
#If we want to get list output of zip
print(list(zip(list1,list2,list3)))  #[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400)]

print('***************InOperator*******************')

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('mykey' in {'mykey':123})

d = {'mykey':123}
print(123 in d.values())
print(123 in d.keys())

print('***************MinMax*******************')

my_list = [10,20,30,40,50]
print(min(my_list))
print(max(my_list))

print('***************RandomLibrary*******************')

from random import shuffle
my_list = [10,20,30,40,50]
shuffle(my_list)  #Shuffle doesn't return anything
print(my_list)

from random import randint
print(randint(0,100))
print(randint(0,100))

print('***************AcceptUserInput*******************')

#Input always accepts anything that's passed into it as a string
num = input("Hey! enter a number here: ")
print(num)
print(type(num))

num1 = int(input("Hey! enter a number here: "))
print(num1)
print(type(num1))