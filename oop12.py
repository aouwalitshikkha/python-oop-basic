class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    # def __repr__(self):


em1 = Employee('Aouwal', 25)
print(em1)

