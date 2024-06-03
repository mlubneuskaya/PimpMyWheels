from src.emulation.customer_decision_maker import create_order
from src.emulation.employee_decision_maker import resigns
from src.models.employee import Employee
from src.models.customer import Customer
from src.models.services import Services
import random


def emulate_day(day, employees, customers, orders, services):
    employee_turnover(day, employees)
    number_of_new_customers = 1  # TODO regular customers
    new_customers = [Customer(day) for _ in range(number_of_new_customers)]
    #orders += [create_order(new_customer, day) for new_customer in new_customers]  # TODO add complaints
    customers += new_customers
    
    for customer in customers:
        for employee in employees:
            if random.choice([True, False]):  # Randomly decide to create a service
                transaction = 1
                service = Services(employee, transaction, customer)
                services.append(service)


def employee_turnover(day, employees_list):
    for employee in employees_list:
        if not employee.resignation_date:
            if resigns(employee, day):
                employee.resignation_date = day
                employees_list.append(Employee(workshop=employee.workshop,
                                               day=day,
                                               position=employee.position,
                                               salary=employee.salary))
