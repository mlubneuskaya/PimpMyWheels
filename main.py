import json
import random

import numpy as np
import pandas as pd

from src.person.customer import Customer
from src.person.employee import Employee
from src.complaint.complaint import Complaint

with open("data\\parameters\\dates.json") as file:
    dates = json.load(file)

with open("data\\parameters\\employees.json") as file:
    employees = json.load(file)

date_range = pd.date_range(dates["start"], periods=dates["length"]).to_pydatetime().tolist()
date_range = [d for d in date_range if d.weekday() < 5]

employees_list = [Employee(*employees[k].values(),
                           dates["start"]) for k in employees.keys()]

customers = [Customer(), Customer()]  # TODO co pierwszym dniem
orders = []
complaints = []


new_customers_number = np.random.randint(0, 3, size=len(date_range))  # TODO inny rozkład
old_customers_number = np.random.randint(0, 1, size=len(date_range))


def orders_creation(new_customers, regular_customers):
    pass


def complaints_creation():
    pass


def emulation(workshop, employees):
    employee_turnover(employees)
    new_customers = [Customer() for _ in range(num_new)]
    regular_customers = []
    orders_creation(new_customers, regular_customers)
    complaints_creation()


def employee_turnover(employees_list):
    for employee in employees_list:  # employees turnover function
        if not employee.quit_date:
            if employee.quits(day.strftime('%d/%m/%Y')):
                employees_list.append(Employee(hire_date=day.strftime('%d/%m/%Y'),
                                               salary=employee.salary,
                                               position=employee.position,
                                               facility=employee.facility))


for day, num_new, num_old in zip(date_range, new_customers_number, old_customers_number):
    employee_turnover(employees_list)
    new_customers = [Customer() for _ in range(num_new)]  # new customer arrival
    for customer in new_customers + [random.choice(customers)]:  # order creation
        order = customer.order()
        orders += [order] if order is not None else []
    customers += new_customers
    for customer in customers:  # complaint creation
        if customer.complains():
            complaints.append(Complaint())

print(len(customers))
