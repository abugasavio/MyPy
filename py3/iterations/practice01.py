
class Player:

    number_of_students = 0

    def __init__(self, name, year, age):
        self.name = name
        self.year = year
        self.age = age
        Player.number_of_students += 1

    def __str__(self):
        return '{}-{}-{}'.format(self.name, self.year, self.age)

    def __repr__(self):
        return 'Player({},{},{})'.format(self.name, self.year, self.age)

    @staticmethod
    def get_students_from_file():
        with open('iterations/file.txt') as f:
            while True:
                line = next(f, None)
                if line is None:
                    break
                yield line.split(',')

    @classmethod
    def create_from_file(cls):
        for student in Player.get_students_from_file():
            yield cls(*student)
