from employees import *

def interface(company):

    x = input("Welcome to Company Manager.\n\nEnter 1 to add an employee.\nEnter 2 to fire an employee.\nEnter 3 to give an employee a raise.\nEnter 4 to see an employee list.\nEnter X to leave the program.\n>> ")
    if x == '1':
        new_emp(company)
    elif x =='2':
        fire_emp(company)
    elif x == '3':
        raise_emp(company)
    elif x == '4':
        print("Employee List\n")
        company.get_employees()
        print("\n")
        interface(company)
    elif x == 'X'.lower():
        exit()
    else:
        print("Not a valid input.")
        interface(company)

def new_emp(company):
    level = input("Enter 1 for Hourly Employee.\nEnter 2 for Salaried Employee.\nEnter 3 for Manager.\nEnter 4 for Executive.\nEnter X to return to the main menu.\n>> ")
    name = input("Enter Name: ")
    pay = float(input("Enter Pay: $"))

    if level == '1':
        new = HourlyEmployee(name, pay)
        company.add_employee(new)

    if level == '2':
        new = SalariedEmployee(name, pay)
        company.add_employee(new)

    if level == '3':
        new = Manager(name, pay)
        company.add_employee(new)

    if level == '4':
        new = Executive(name, pay)
        company.add_employee(new)

    if level == 'x'.lower():
        interface(company)
    interface(company)

def fire_emp(company):
    emp = input("Give the name of the employee you wish to fire: ")
    for e in company.employee_list:
        if e.name == emp:
            company.fire_employee(e)
    interface(company)

def raise_emp(company):
    emp = input("Give the name of the employee you wish to give a raise: ")
    for e in company.employee_list:
        if e.name == emp:
            e.give_raise()
    interface(company)
