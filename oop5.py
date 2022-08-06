class Product:
    def __init__(self, name: str, price: float, quantity: int, discount = 0):
        # Data validation
        assert price >= 0, 'Price must be greater than 0'
        assert quantity >= 0, 'Quantity must be greater than 0'
        assert discount >= 0, 'Discount must be greater than 0'

        # Assign to objects
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def total_price(self):
        return self.price * self.quantity

    def net_payable(self):
        main_percentage = 1 - self.discount/100
        net_amount = self.price * self.quantity * main_percentage
        return net_amount


items = Product('Mobile Phone', 8000, 150)
item2 = Product('Laptop', 10000, 100)
item3 = Product('Moneybag', 280, 15, 10 )

# print(items.price)
# print(items.total_price())
print(item3.net_payable())