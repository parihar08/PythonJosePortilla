s = set()

print('*********ADD************','\n')

s.add(1)
s.add(2)
print(s)        #{1, 2}

print('*********CLEAR************','\n')
s.clear()
print(s)        #set()

print('*********COPY************','\n')
s = {1,2,3}
sc = s.copy()
print(sc)       #{1, 2, 3}

print('*********DIFFERENCE************','\n')
s.add(4)
print(s)
print(sc)
print(s.difference(sc))

print('*********DIFFERENCE UPDATE************','\n')

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)    #Returns s1 after removing all the elements found in s2
print(s1)                   #{2, 3}

print('*********DISCARD************','\n')
#Removes element from a set if it is a member
print(s)                    #{1, 2, 3, 4}
s.discard(2)
print(s)                    #{1, 3, 4}

print('*********INTERSECTION************','\n')
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))

print('*********INTERSECTION UPDATE************','\n')
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection_update(s2)  #It will update s1 to intersection of s1 and s2
print(s1)                   #{1, 2}

print('*********IS DISJOINT************','\n')
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

#This method will return True if 2 sets has NULL intersection
print(s1.isdisjoint(s2))    #False
print(s1.isdisjoint(s3))    #True

print('*********IS SUBSET************','\n')
s1 = {1,2}
s2 = {1,2,4}
print(s1.issubset(s2))      #True

print('*********IS SUPERSET************','\n')
s1 = {1,2}
s2 = {1,2,4}
print(s2.issuperset(s1))    #True

print('*********SYMMETRIC DIFFERENCE************','\n')
#Will return all the elements which are only in one of the sets.Opposite of Intersection
s1 = {1,2}
s2 = {1,2,4}
print(s1.symmetric_difference(s2))      #4

print('*********UNION************','\n')
s1 = {1,2}
s2 = {1,3,4}
print(s1.union(s2))         #{1, 2, 3, 4}

print('*********UPDATE************','\n')
#Returns the same result as union
s1.update(s2)
print(s1)                   #{1, 2, 3, 4}
