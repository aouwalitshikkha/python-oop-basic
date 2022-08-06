class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


items = Product('Mobile Phone', 8000, 10 )
item2 = Product('Laptop', 10000, 100 )

# def add(a,b):
#     return a+b

print(items.price)
print(items.quantity)
print(items.name)

print(item2.name)
print(item2.price)
print(item2.quantity)