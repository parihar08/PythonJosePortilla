#For loops are used to execute a block of code for every iteration
#We can iterate over every character in a String
#Iterate over every item in a list
#Iterate over every key in a dictionary

my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)

print('***************CheckEvenNumbers*******************')
for num in my_list:
    if num%2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

print('***************SumOfNumbersInAList*******************')
list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(list_sum)

print('***************ForLoopsWithStrings*******************')
my_string = 'Hello World'
for s in my_string:
    print(s)

print('***************ForLoopsWithTuples*******************')
my_tuple = (1,2,3,4,5)
for item in my_tuple:
    print(item)

print('***************ForLoopsWithListOfTuples*******************')
my_list1 = [(1,2),(3,4),(5,6),(7,8)]
print(len(my_list1))
for item in my_list1:
    print(item)

print('***************TuplesUnpacking*******************')
for a,b in my_list1:
    print(a)
    print(b)

print('*************************************************')
my_list2 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in my_list2:
    print(b)

print('***************ForLoopsWithDictionaries*******************')
my_dict = {'k1':1,'k2':2,'k3':3}
for item in my_dict:
    print(item)  #Returns only the keys

for item in my_dict.items():
    print(item) #Returns key value pair in the form of Tuple ('k1',1) ('k2',2) ('k3',3)

for key,value in my_dict.items():
    print(value) #To get the values from a dictionary, use the tuple unpacking technique

for value in my_dict.values():
    print(value) #Will only print out the values