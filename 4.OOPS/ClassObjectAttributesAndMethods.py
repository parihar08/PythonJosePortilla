class Dog():

    #Class Object Attribute
    #Same for any instance of a class
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    #Methods - Function inside a class - Operations/Actions
    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog(breed='Husky',name='Jackie',spots=True)
print(my_dog.name+' is of '+my_dog.breed+ ' breed and has spots')
my_dog.bark(1) #Calling method using class instance

print('*********************************************')

my_dog1 = Dog(breed='Lab',name='Sammy',spots=False)
print(my_dog1.name+' is of '+my_dog1.breed+ ' breed and has no spots')
my_dog1.bark(2)

print('*********************************************')

my_dog2 = Dog('Lab','Frankie',False)
print(my_dog2.name+' is of '+my_dog2.breed+ ' breed and has no spots')
my_dog2.bark(3)


print('*********************************************')

class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self,radius=1): #default value=1
        self.radius = radius
        self.area = radius*radius*self.pi
        #self.area = radius * radius * Circle.pi #We can use classname.classobjectattribute

    #METHOD
    def get_circumference(self):
        return 2*self.pi*self.radius

my_circle = Circle()
print(my_circle.get_circumference())
print(my_circle.area)

print('*********************************************')

my_circle1 = Circle(30)
print(my_circle1.get_circumference())
print(my_circle1.area)