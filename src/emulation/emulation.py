import random

from scipy import stats

from src.emulation.customer_decision_maker import create_order, create_complaint
from src.emulation.employee_decision_maker import resigns
from src.models.customer import Customer
from src.models.employee import Employee
from src.models.services import Services


def emulate_day(date, employees, customers, inactive_customers, orders, complaints):
    employee_turnover(date, employees)
    complaints_creation(date, orders, complaints)
    customers_today = customers_arrival(date, customers)
    orders_creation(date, customers_today, employees, orders)
    customers += customers_today
    accounts_deactivation(date, customers, inactive_customers)


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


def customers_arrival(date, customers):
    number_of_new_customers = stats.poisson.rvs(4)  # TODO move the expected value to parameters json
    new_customers = [Customer(date) for _ in range(number_of_new_customers)]
    number_of_regular_customers = stats.poisson.rvs(0.01 * len(customers))  # TODO move the expected value to parameters
    regular_customers = []
    if number_of_regular_customers <= len(customers):
        regular_customers = random.sample(customers, k=number_of_regular_customers)  # TODO add weights
    for customer in regular_customers:
        customer.last_active = date
    return new_customers + regular_customers


def orders_creation(date, customers, employees, orders):
    employee = employees[0]
    orders += [create_order(customer, employee, date) for customer in customers]


def accounts_deactivation(date, customers, inactive_customers):
    number_of_accounts_to_deactivate = stats.poisson.rvs(0.001 * len(customers))
    # TODO move the expected value to parameters
    if number_of_accounts_to_deactivate <= len(customers):
        accounts_to_deactivate = random.sample(customers, k=number_of_accounts_to_deactivate)
        for account in accounts_to_deactivate:
            account.account_deletion_date = date
            customers.remove(account)
        inactive_customers += accounts_to_deactivate
