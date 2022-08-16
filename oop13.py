class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.age == other.age


em1 = Employee('Aouwal', 25)
em2 = Employee('Aouwal', 25)
print(em1 == em2)

