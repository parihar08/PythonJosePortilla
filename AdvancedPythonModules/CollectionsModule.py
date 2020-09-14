# Counter
# DefaultDictionary
# Named Tuple

from collections import Counter
#Counter is a dictionary sub-class.
#Elements are stored as Dictionary KEYS and Counts are stored as VALUES
print('*****************COUNTER***********************')

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3]

#Get count of each unique items in the list
print(Counter(mylist))

print('****************************************')

mylist = ['a','a',1,2,3,3]
print(Counter(mylist)) #Counter({'a': 2, 3: 2, 1: 1, 2: 1})

print('****************************************')

print(Counter('aaaabbbffffkfhjfbvahfvkfb'))

print('****************************************')

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.lower().split()))

print('****************************************')

#Common patters we encounter using the Counter object

letters = 'aaabbbbcccccccdddddddddd'

c = Counter(letters)
print(c)
print(c.keys())
print(c.items())
print(c.most_common())  #Returns a list of tuples
print(c.most_common(2)) #Returns 2 most common

print('****************************************')
my_list = [1,1,1,1,3,4,5,3,4,5,3,4,5,6,8,6,7,8,6,5,7,4,6,7]
a = Counter(my_list)

print(a.most_common())  #Returns most common
print(sum(a.values()))  #Total of all counts
print(list(a))          #Lists unique elements
print(set(a))           #Converts to set
print(dict(a))          #Converts to a regular dictionary
print(a.items())        #Converts to list of (elem,count) pairs
print(a.clear())        #Resets all counts

print('****************DEFAULT DICTIONARY************************')

from collections import defaultdict

d = {'a':10}
print(d)
print(d['a'])
#print(d['b'])  #KeyError: 'b' as 'b' is not part of dictionary
print('****************************************')
#Default Dict will assign a default value in an instance where KeyError will occur

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['wrong key!'])  #Default dict value 0 assigned in case KeyError could have occurred
print(d)

print('****************NAMED TUPLE************************')
#Named Tuple tries to expand on a normal tuple object by actually having name in the indices
#Named tuples are basically easy-to-create, lightweight object types. Named tuple instances
#can be referenced using object-like variable dereferencing or the standard tuple syntax.
#They can be used similarly to struct or other common record types, except that they are
#immutable.

my_tuple = (10,20,30)

print(my_tuple[0])

print('****************************************')

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy[0])
print(sammy.breed)
print(sammy[1])
print(sammy.name)
print(sammy[2])



