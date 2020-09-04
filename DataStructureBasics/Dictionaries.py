#Dictionaries are unordered mappings for storing objects
#Use key-value pair {'key1':'value1','key2':'value2'}

#Dictionaries are objects retrieved by key.They are unordered and cannot be sorted
#Lists are objects retrieved by location - Ordered sequence can be indexed or sliced

print('****************************************************')
print('************CreateDictionary************************')

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
#Getting a value from dictionary
print(my_dict['key1'])

price_lookup = {'apples':2.99,'oranges':1.99,'milk':4.95}
print(price_lookup['apples'])

print('************NestedDictionary************************')
#Dictionaries can contain string,list or even another dictionary
nested_dict = {'k1':123,'k2':[4,5,6],'k3':{'insideKey':100}}
print(nested_dict['k2'])
print(nested_dict['k2'][2]) #Grab element from list within a dictionary
print(nested_dict['k3'])
print(nested_dict['k3'])
print(nested_dict['k3']['insideKey']) #Grab element from dictionary within a dictionary


d = {'key1': ['a','b','c']}
my_list = d['key1']
print(my_list)         #['a', 'b', 'c']
letter = my_list[2]
print(letter)          #c
print(letter.upper())  #C

#Stack all in one step
print(d['key1'][2].upper())

print('************AddElementsToADictionary************************')
d1 = {'k1':100,'k2':200}
print(d1)
d1['k3'] = 300
print(d1)
#Overwrite existing key value
d1['k1'] = 'NEW VALUE'
print(d1)

print('************DictionaryMethods************************')
d2 = {'k1':100,'k2':200,'k3':300}
#Find All Keys of a dictionary
print(d2.keys())
#Find All Values of a dictionary
print(d2.values())
#Return all the dictionary pairings
print(d2.items())  #Returns a list of tuples

print('****************************************************')

#Grab hello from the dictionary
nested_dict1 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(nested_dict1['k1'][2]['k2'][1]['tough'][2][0])