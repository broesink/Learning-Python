class Car:
    def __init__(self, brand, model, year):
        #self > This specific object
        #self.brand = the 'brand' variable from this object
        #brand = The value that it gets when creating
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 #it is always 0 at creation
    
    def drive(self, km):
        self.mileage += km
        print(f'Drove {km}km. Total: {self.mileage}km')

my_car = Car('BMW', '320d', 2003)
my_car.drive(100)
my_car.drive(99)
print(my_car.mileage)