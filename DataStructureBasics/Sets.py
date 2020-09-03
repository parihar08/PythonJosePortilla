#Sets are unordered collections of unique elements
#There cannot be duplicates in a set
# Set {1,2,3}

print('****************************************************')
print('***************Sets*********************')
my_set = set()
my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)

print(set('Mississippi'))  #Sets don't have duplicates or any particular order

print('***************ListToSets*********************')
my_list = [1,1,1,1,3,3,3,4,4,4,4,4]
print(my_list)
print(set(my_list))  #{1,3,4}#Sets don't have duplicates or any particular order