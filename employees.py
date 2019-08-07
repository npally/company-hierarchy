class Employee():

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def __str__(self):
        return self.name

class HourlyEmployee(Employee):

    level = "Hourly Employee"

    def get_wage(self):
        return 'Hourly: $' + format(self.pay, ',.2f')

    def give_raise(self):
        self.pay = self.pay * 1.1

    def get_string(self):
        return self.name + ": " + self.level + "| Pay- " + self.get_wage()

class SalariedEmployee(Employee):

    level = "Salaried Employee"

    def get_wage(self):
        return 'Annually: $' + format(self.pay, ',.2f')

    def give_raise(self):
        self.pay = self.pay * 1.2

    def get_string(self):
        return self.name + ": " + self.level + "| Pay- " + self.get_wage()

class Manager(Employee):

    level = "Manager"

    def get_wage(self):
        return 'Annually: $' + format(self.pay, ',.2f')

    def give_raise(self):
        self.pay = self.pay * 1.25

    def get_string(self):
        return self.name + ": " + self.level + "| Pay- " + self.get_wage()

class Executive(Employee):

    level = "Executive"

    def get_wage(self):
        return 'Annually: $' + format(self.pay, ',.2f')

    def give_raise(self):
        self.pay = self.pay * 1.3

    def get_string(self):
        return self.name + ": " + self.level + "| Pay- " + self.get_wage()

class Company():

    def __init__(self, name):
        self.name = name
        self.employee_list = []

    def add_employee(self, emp):
        self.employee_list.append(emp)

    def fire_employee(self, emp):
        self.employee_list.remove(emp)

    def get_employees(self):
        for e in self.employee_list:
            print(e.get_string())
