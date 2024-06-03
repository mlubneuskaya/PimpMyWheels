from src.models.complaint import Complaint
from src.models.services import Services


def create_order(customer, day):
    customer.last_active = day
    return Services()


def create_complaint(customer, day):
    customer.last_active = day
    return Complaint()
