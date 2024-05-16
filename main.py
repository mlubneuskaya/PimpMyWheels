import json
import pandas as pd

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


for day in date_range:
    for employee in employees_list:
        if not employee.quit_date:
            if employee.quits(day.strftime('%d/%m/%Y')):
                employees_list.append(Employee(hire_date=day.strftime('%d/%m/%Y'),
                                               salary=employee.salary,
                                               position=employee.position,
                                               facility=employee.facility))


print(len(employees_list))

