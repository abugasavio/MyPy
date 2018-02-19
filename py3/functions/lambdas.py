students = ["Savio", "John", "Michael", "andrew"]

sorted_students = sorted(students, key=lambda name: name.lower())

print(sorted_students)


def is_even(number):
    return number % 2 == 0


print([number for number in range(200) if is_even(number)])
