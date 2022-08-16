class Employee:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.age == other.age

    def works(self):
        print(f'{self.name} is working')


class SoftEngineer(Employee):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def works(self):
        print(f'{self.name} is doing code')


class Designer(Employee):
    def __init__(self, name, age, software):
        super().__init__(name, age)
        self.software = software

    def works(self):
        print(f'{self.name} is doing design in {self.software}')


em1 = Employee('Aouwal', 25)
em1.salary(25)