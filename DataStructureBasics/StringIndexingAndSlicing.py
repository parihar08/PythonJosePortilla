#String Indexing
string = "Hello World"
print(string[0])
print(string[9])
print(string[-2])

#String Slicing
string = "abcdefghijk"
print(string[2:]) #from letter c to the end
print(string[:3]) #from beginning to the letter c
print(string[3:6]) #grab def
print(string[1:3]) #grab bc
print(string[::]) #step size=1
print(string[::3]) #step size=3
print(string[2:7:2]) #step size=2
print(string[::-1]) #step size=-1 Reverse the string