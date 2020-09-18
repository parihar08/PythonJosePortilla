class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# myanimal = Animal()
# myanimal.who_am_i()
# myanimal.who_am_i()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self) #Create instance of Animal class when we create instance of Dog class
        print('DOG CREATED')

    #METHOD OVERRIDE
    def who_am_i(self):
        print("I am a Dog")

    #ADDITIONAL METHODS
    def bark(self):
        print('WOOF!')

mydog = Dog()
print('*********************************************')
mydog.who_am_i()
mydog.bark()
mydog.eat()

print('*******************POLYMORPHISM**************************')
#Different object classes can share the same method name

class Dog1():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF!"

class Cat1():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW!"

niko = Dog1('niko')
felix = Cat1('felix')

print(niko.speak())
print(felix.speak())

print('*********************************************')

#Here both Dog1 and Cat1 class has speak() method
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

print('*********************************************')

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

print('*******************ABSTRACT CLASSES & INHERITANCE**************************')

class Animal2():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError('SubClass must implement this abstract method!!')

#myanimal = Animal2('fred')

class Dog2(Animal2):

    def speak(self):
        return self.name + " says WOOF!"

class Cat2(Animal2):

    def speak(self):
        return self.name + " says MEOW!"

fido = Dog2('Fido')
isis = Cat2('Isis')

print(fido.speak())
print(isis.speak())

