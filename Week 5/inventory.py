class Product:
    
    total_products = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1

    def __str__(self):
        return f'{self.name} | €{self.price:.2f} | {self.stock} in stock'

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError
        else:
            self._price = value

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError
        else:
            self._stock = value

    def restock(self, amount):
        if amount <= 0:
            raise ValueError
        self.stock += amount

    def sell(self, sale):
        if sale <= 0:
            raise ValueError
        if sale > self.stock:
            raise ValueError
        self.stock -= sale


product1 = Product('Milk', 1, 200)
product2 = Product('Yoghurt', 2, 50)
product3 = Product('Cheese', 5, 75)

print(f'Total products = {Product.total_products}')

product1.restock(50)

print(product1)
print(product2)
print(product3)

try:
    product1.price = 0
except ValueError:
    print('Oooops')

try:
    product1.sell(-5)
except ValueError:
    print('Invalid sale')


print(product1.price)
print(product2.price)
print(product3.price)

product1.sell(20)
print(product1)