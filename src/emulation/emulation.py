import random

from scipy import stats

from src.emulation.customer_decision_maker import create_complaint


def emulate_day(date, workshop_decision_makers, customer_decision_maker, transactions):
    customer_decision_maker.accounts_deactivation(date)
    for wdm in workshop_decision_makers:
        wdm.employee_turnover(date)
        wdm.complete_repairs(date)
    customers_today = customer_decision_maker.customers_arrival(date)
    for customer in customers_today:
        wdm = random.choice(workshop_decision_makers)
        transactions.append(wdm.add_service_and_create_transaction(date, customer))


def complaints_creation(date, orders, complaints):
    number_of_orders_to_be_complained_about = stats.poisson.rvs(0.001 * len(orders))  # TODO add weights
    if number_of_orders_to_be_complained_about <= len(orders):
        orders_to_be_complained_about = random.sample(orders, k=number_of_orders_to_be_complained_about)
        complaints += [create_complaint(order, date) for order in orders_to_be_complained_about]
