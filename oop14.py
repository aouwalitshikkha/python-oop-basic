class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.age == other.age


class SoftEngineer(Employee):
    pass


class Designer(Employee):
    pass


se1 = SoftEngineer('Aouwal', 25)
d1 = Designer('Samrat', 26)

print(se1.name)
print(d1.name)
