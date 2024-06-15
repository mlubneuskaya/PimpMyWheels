import random

from scipy import stats

from src.models.complaint import Complaint
from src.models.customer import Customer
from src.models.services import Services


def create_order(customer, employee, day):
    customer.last_active = day
    transaction = 1
    return Services(customer=customer, employee=employee, transaction=transaction)


def create_complaint(customer, open_date, employee, service, closure_date, description, cost):
    customer.last_active = open_date
    return Complaint(
        employee,
        service,
        open_date,
        closure_date,
        description,
        cost
    )


class CustomerDecisionMaker:
    def __init__(self, account_deactivation_probability,
                 purchase_probability,
                 selling_probability,
                 repair_probability,
                 regular_customers_per_day,
                 new_customers_per_day):
        self.account_deactivation_probability = account_deactivation_probability
        self.order_types = ["repair", "buy", "sell"]
        self.order_probabilities = [repair_probability, purchase_probability, selling_probability]
        self.active_customers = []
        self.all_customers = []
        self.regular_customers_per_day = regular_customers_per_day
        self.new_customers_per_day = new_customers_per_day

    def accounts_deactivation(self, date):
        number_of_accounts_to_deactivate = stats.poisson.rvs(
            self.account_deactivation_probability * len(self.active_customers))
        if number_of_accounts_to_deactivate <= len(self.active_customers):
            accounts_to_deactivate = random.sample(self.active_customers, k=number_of_accounts_to_deactivate)
            for account in accounts_to_deactivate:
                account.account_deletion_date = date
                self.active_customers.remove(account)

    def customers_arrival(self, date):
        number_of_new_customers = stats.poisson.rvs(self.new_customers_per_day)
        new_customers = [Customer(date) for _ in range(number_of_new_customers)]
        number_of_regular_customers = stats.poisson.rvs(
            self.regular_customers_per_day * len(self.active_customers))
        regular_customers = []
        if number_of_regular_customers <= len(self.active_customers):
            regular_customers = random.sample(self.active_customers, k=number_of_regular_customers)
        for customer in regular_customers:
            customer.last_active = date
        self.active_customers += new_customers
        self.all_customers += new_customers
        return new_customers + regular_customers

