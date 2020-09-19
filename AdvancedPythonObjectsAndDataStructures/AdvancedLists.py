l = [1,2,3]

print('*********APPEND************','\n')

l.append(4)
print(l)

print('*********COUNT************','\n')
print(l.count(2))

print('*********EXTEND************','\n')
x = [1,2,3]
x.append([4,5]) #Appends adds all the elements to the list
print(x)        #[1, 2, 3, [4, 5]]

print('*********************************','\n')

x = [1,2,3]
x.extend([4,5]) #Extends 4,5 to the original list
print(x)        #[1, 2, 3, 4, 5]

print('*********INDEX************','\n')
x=[1,2,3,4]
print(x.index(2))   #1
print(x.index(4))   #3
#print(x.index(5))  #ValueError: 5 is not in list

print('*********INSERT************','\n')
x=[1,2,3,4]
x.insert(2,'Inserted')
print(x)            #[1, 2, 'Inserted', 3, 4]

print('*********POP************','\n')
x=[1,2,3,4]
x.pop()
print(x)            #[1, 2, 3]
x.pop(0)
print(x)            #[2, 3]

print('*********REMOVE************','\n')
#Removes the first occurrence of a value
x = [1,2,3,4,1,2,3]
x.remove(2)
print(x)            #[1, 3, 4, 1, 2, 3]

print('*********REVERSE************','\n')

x = [1,2,3,4,5,6]
x.reverse()
print(x)            #[6, 5, 4, 3, 2, 1]

print('*********REVERSE************','\n')

x = [3,4,2,1]
x.sort()
print(x)            #[1,2,3,4]