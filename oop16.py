class Product:
    def __init__(self, price):
        self.price = price
        self.__final_price = price + price * 0.15

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self,discount):
        self.__final_price = self.__final_price - self.calculate_discount(discount)
        return self.__final_price

    def __calculate_discount(self, discount):
        return self.__final_price * (discount/100)


obj = Product(100)
print(obj.get_final_price())
print(obj.set_final_price(10))
print(obj.calculate_discount(10))



