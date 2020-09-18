class Dog():
    #Constructor for a class
    def __init__(self,mybreed,name,spots):
        #Attributes
        #We take in the arugument - mybreed
        #And assign it using self.argument  e.g. self.mybreed
        self.breed = mybreed
        self.name = name
        #Expect boolean True/False
        self.spots = spots

my_dog = Dog(mybreed='Husky',name='Jackie',spots=True)
print(type(my_dog))
print(my_dog.name+' is of '+my_dog.breed+ ' breed and has spots')
print(my_dog.name)
print(my_dog.spots)

print('****************************************')