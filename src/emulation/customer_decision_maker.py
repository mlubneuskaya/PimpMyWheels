from src.models.complaint import Complaint
from src.models.services import Services


def create_order(customer, employee,  day):
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
