from src.emulation.customer_decision_maker import create_order
from src.emulation.employee_decision_maker import quits
from src.models.models import Employee, Customer


def emulate_day(day, employees, customers, orders):
    employee_turnover(day, employees)
    number_of_new_customers = 1  # TODO regular customers
    new_customers = [Customer(day) for _ in range(number_of_new_customers)]
    orders += [create_order(new_customer, day) for new_customer in new_customers]  # TODO add complaints
    customers += new_customers


def employee_turnover(day, employees_list):
    for employee in employees_list:
        if not employee.quit_date:
            if quits(employee, day):
                employee.quit_date = day
                employees_list.append(Employee(workshop=employee.workshop,
                                               day=day,
                                               position=employee.position,
                                               salary=employee.salary))
