from src.models.services import Services
from src.models.complaint import Complaint


def create_order(customer, day):
    customer.last_active = day
    return Services()


def create_complaint(customer, day):
    customer.last_active = day
    return Complaint()
