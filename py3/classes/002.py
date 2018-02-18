# class variables


class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employee += 1


print(Employee.__dict__)

