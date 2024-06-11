from src.models.complaint import Complaint
from src.models.services import Services


def create_order(customer, employee,  day):
    customer.last_active = day
    transaction = 1
    return Services(customer=customer, employee=employee, transaction=transaction)


def create_complaint(customer, day):
    customer.last_active = day
    return Complaint()
