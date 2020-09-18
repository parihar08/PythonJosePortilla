#List Comprehensions are a unique way of quickly create a list in python

print('*******************************************')

mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)

print('*****************ListComprehension**************************')

mystring = 'hello'
mylist1 = [letter for letter in mystring] #flattened out for loop using list comprehension
print(mylist1)

print('*******************************************')

mylist2 = [x for x in 'word']
print(mylist2)

mylist3 = [x for x in range(0,11)]
print(mylist3)

#Grab square of every number in the range
mylist4 = [x**2 for x in range(0,11)]
print(mylist4)

print('*****************AddIfStatementInListComprehension**************************')

#Grab even numbers
mylist5 = [x for x in range(0,11) if x%2==0]
print(mylist5)

print('*******************************************')

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

print('*****************UseIfElseStatementInListComprehension**************************')

#Order is different when using if and else with list comprehension
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

print('*****************NestedLoopsInListComprehension**************************')

list6 = []
for x in [2,4,6]:
    for y in[3,5,7]:
        list6.append(x*y)
print(list6)

#Using List Comprehension
list7 = [x*y for x in [2,4,6] for y in[3,5,7]]
print(list7)

print('*******************************************')

st = 'Create a list of the first letters of every word in this string'
list8 = [x[0] for x in st.split(' ')]
print(list8)