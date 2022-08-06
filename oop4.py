class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


items = Product('Mobile Phone', 8000, 150)
item2 = Product('Laptop', 10000, 100)

print(items.price)
print(items.total_price())
