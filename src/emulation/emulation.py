import random

from scipy import stats

from src.emulation.customer_decision_maker import create_order, create_complaint
from src.emulation.employee_decision_maker import resigns
from src.models.employee import Employee


def emulate_day(date, employees, customer_decision_maker, orders, complaints):
    customer_decision_maker.accounts_deactivation(date)
    employee_turnover(date, employees)
    # complaints_creation(date, orders, complaints)
    customers_today = customer_decision_maker.customers_arrival(date)
    orders_creation(date, customers_today, employees, orders)

def employee_turnover(day, employees_list):
    for employee in employees_list:
        if not employee.resignation_date:
            if resigns(employee, day):
                employee.resignation_date = day
                employees_list.append(Employee(workshop=employee.workshop,
                                               day=day,
                                               position=employee.position,
                                               min_salary=employee.min_salary,
                                               avg_salary=employee.avg_salary,
                                               max_salary=employee.max_salary))


def complaints_creation(date, orders, complaints):
    number_of_orders_to_be_complained_about = stats.poisson.rvs(0.001 * len(orders))  # TODO add weights
    if number_of_orders_to_be_complained_about <= len(orders):
        orders_to_be_complained_about = random.sample(orders, k=number_of_orders_to_be_complained_about)
        complaints += [create_complaint(order, date) for order in orders_to_be_complained_about]


def orders_creation(date, customers, employees, orders):
    employee = employees[0]
    orders += [create_order(customer, employee, date) for customer in customers]
