class Product():
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def show(self):
        print(f'''{self.name}:
Quantity: {self.quantity}
Price: {self.price}''')

class Beverage(Product):
    def __init__(self, name, quantity, price,additional):
        super().__init__(name, quantity, price)
        self.additional = additional
    def show(self):
        print(f''' {self.name}:
Quantity: {self.quantity}
Price: {self.price}
Additional: {self.additional}''')

class Food(Product):
    def __init__(self, name, quantity, price, additional):
        super().__init__(name, quantity, price)
        self.additional = additional
    def show(self):
        print(f''' {self.name}:
Quantity: {self.quantity}
Price: {self.price}
Additional: {self.additional}''')