class Product:
    '''
    These data will show the details of product class.
    Here discount rate is defauls 10, it will take name as string,price as float etc
    '''
    discount = 10
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # Data validation
        assert price >= 0, 'Price must be greater than 0'
        assert quantity >= 0, 'Quantity must be greater than 0'

        # Assign to objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #  Action to append the list
        Product.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def net_payable(self):
        main_percentage = 1 - self.discount/100
        net_amount = self.price * self.quantity * main_percentage
        return net_amount

    def __repr__(self):
        return "Product("+self.name+','+str(self.price)+','+ str(self.quantity)+' )'


items = Product('Mobile Phone', 8000, 150)
item2 = Product('Laptop', 10000, 100)
item3 = Product('Moneybag', 280, 15)

print(Product.all)
