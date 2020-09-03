#Tuples are similar to lists having one difference - Immutability
#Once element is inside a tuple it cannot be reassigned
#Tuples use parenthesis: (1,2,3)
#Tuples are used when we are passing around objects in our program and make sure they don't accidently change

print('****************************************************')
print('***************Tuples*********************')
t = (1,2,3)
list = [1,2,3]
print(type(t))
print(type(list))

t1 = ('one',2,'3.0')
print(t1)

print('***************SlicingAndIndexing*********************')
print(t1[0])
print(t1[-1])

print('***************TupleMethods*********************')

t2 = ('a','a','b')
print(t2.count('a'))  #Count() returns how many times an element is present in tuple
print(t2.index('a'))  #Index() returns the index of first occurrence of an element in tuple

print('***************TupleImmutability*********************')
t3 = (1,2,3)
list3 = [1,2,3]
list3[0] = 'NEW'
#t3[0] = 'NEW'  #Not allowed in tuple. Tuple object doesn't support item assignment
print(list3)