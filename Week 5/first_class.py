#Class definition, the blueprint
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f'{self.name} says: Woof!')

    def info(self):
        print(f'{self.name} is a {self.age} year old {self.breed}')

#Next, create the instances from the blueprint
dog1 = Dog('Rex', 'German Shepherd', 3)
dog2 = Dog('Bella', 'Labrador', 5)

#Call the methods on an instance
dog1.bark()
dog2.info()

#Aproach an instance variable right away
print(dog1.name)
print(dog2.age)

#Adjust variable
dog1.age = 4
print(dog1.age)