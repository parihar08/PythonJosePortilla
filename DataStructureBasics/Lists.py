# [1,2,3,4,5]
# Lists Support indexing and slicing. List can be nested
# Lists are Mutable

list1 = [1,2,3]
list2 = ['abc',1,2,30.2]
print(len(list2))

print('************ListIndexingAndSlicing************************')

#List Indexing and Slicing
list3 = ['one','two','three']
print(list3)
print(list3[0])
print(list3[1:])

print('***************NestedList*********************')

#Nested List

nested_list=[1,2,[3,4]]
print(nested_list[2][1]) #Will print 4
print(nested_list[2][0]) #Will print 3
print(nested_list[1])    #Will print 2

print('****************ListConcatenation********************')

#Concatenate List
print(list3+list2)
list4 = list3 + list2
print(list4)

list4[0] = 'ONE ALL CAPS'  #Lists are Mutable - change elements ina list
print(list4)

print('***************AppendList*********************')

#Add element to end of list using Append()
print(list3)
list3.append('four')
print(list3)
list3.append('five')
print(list3)

print('*****************PopList*******************')

#Remove element from the list using Pop()
list3.pop()
print(list3)
list3.pop(2) #Remove from a specific index
print(list3)

print('****************SortList********************')

#Sorting
list5=['e','s','a','g','t','n']
list6=[4,6,2,5,9,3]
list5.sort()  #Sorted in Ascending Order. This method doesn't return anything and is of type None
list6.sort()
print(list5)
print(list6)

print('****************ReverseList********************')

#Reverse
list5.reverse()
print(list5)
list6.reverse()
print(list6)

print('************************************')