#Special methods allows us to use builtin operations like length or print function with
#our own user created objects

mylist = [1,2,3,4,5]
print(len(mylist))
print((mylist))

print('*********************************************')

class Sample():
    pass

mysample = Sample()
# print(len(mysample))  #This will give error as we can not use len function directly with our object
# print(mysample)

print('******************MAGIC|DUNDER METHODS***************************')
#Special methods start with __(double underscores)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book('Python Rocks','Jose',200)

#Print function tries to find string representation of b
print(b)      #Output: <__main__.Book object at 0x7fe46a26d1c0>
print(str(b)) #Output: <__main__.Book object at 0x7fe46a26d1c0>
#print(len(b)) #TypeError: object of type 'Book' has no len()


print('*********************************************')

class Book1():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    #This special method can be used by any function which ask for string representation
    #of a class.e.g. print and len functions
    def __str__(self):
        return f'{self.title} by {self.author}'

    #For length function, below is the special method
    def __len__(self):
        return self.pages

    # Delete a object - It will delete the object (b or b1) from the memory of computer
    # del b
    def __del__(self):
        print('A book object has been deleted')

b1 = Book1('Python Rocks','Jose',200)
#Print function tries to find string representation of b and here __string__ method is found
print(b1)
print(str(b1))
print(len(b1))
del b1





