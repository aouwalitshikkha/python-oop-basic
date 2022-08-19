class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.full_name = f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'


p1 = Person('Abdul', 'Aouwal')
p1.last = 'Awal'
print(p1.email)