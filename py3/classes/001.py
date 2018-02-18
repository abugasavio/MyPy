# Python Object-Oriented Programming


class Employee:
    def __init__(self, first_name, last_name, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp1 = Employee('Savio', 'Abuga', 'savioabuga', 'michael', email='savioabuga@gmail.com')


emp1.first_name = 'Savio'
emp1.email = 'John'


print(emp1)
