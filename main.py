import json

import numpy as np
import pandas as pd

from src.person.customer import Customer
from src.person.employee import Employee

with open("data\\parameters\\dates.json") as file:
    dates = json.load(file)

with open("data\\parameters\\employees.json") as file:
    employees = json.load(file)

date_range = pd.date_range(dates["start"], periods=dates["length"]).to_pydatetime().tolist()
date_range = [d for d in date_range if d.weekday() < 5]

employees_list = [Employee(*employees[k].values(),
                           dates["start"]) for k in employees.keys()]

customers_list = []


def handle_order(order):
    pass


new_customers_number = np.random.randint(0, 3, size=len(date_range))  # inny rozkład
old_customers_number = np.random.randint(0, 1, size=len(date_range))

for day, num in zip(date_range, new_customers_number, old_customers_number):
    for employee in employees_list:
        if not employee.quit_date:
            if employee.quits(day.strftime('%d/%m/%Y')):
                employees_list.append(Employee(hire_date=day.strftime('%d/%m/%Y'),
                                               salary=employee.salary,
                                               position=employee.position,
                                               facility=employee.facility))
    new_customers = [Customer() for _ in range(num)]
    for customer in new_customers:
        order = customer.order()
        handle_order(order)
    customers_list.append(new_customers)

print(len(customers_list))
