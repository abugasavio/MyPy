my_student = {
    'name': 'Savio Abuga',
    'grades': [70, 88, 90, 99]
}


def average_marks(student):
    return sum(student['grades']) / len(student['grades'])
