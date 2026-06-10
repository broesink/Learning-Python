#A method is a function that belongs to a class. The difference with a seperate function is that it has access to all data of the object via self

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        '''Add an item to the shopping cart'''
        self.items.append({'name': name, 'price': price})
        print(f'Added: {name} (€{price:.2f})')

    def remove_item(self, name):
        '''Delete an item based on the name'''
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                print(f'Removed: {name}')
                return
        print(f'{name} not found in cart')

    def get_total(self):
        '''Calculate the total amount'''
        return sum(item['price'] for item in self.items)

    def show(self):
        if not self.items:
            print('Your cart is empty.')
            return
        print('\n--- Shopping Cart ---')
        for item in self.items:
            print(f'   {item["name"]:20} €{item["price"]:.2f}')
        print(f'   {"TOTAL":20} €{self.get_total():.2f}')
        print('-------------------------') 

#use them
cart = ShoppingCart()
cart.add_item('Laptop', 1299.99)
cart.add_item('Mouse', 29.99)
cart.add_item('Keyboard', 79.99)
cart.remove_item('Mouse')
cart.show()