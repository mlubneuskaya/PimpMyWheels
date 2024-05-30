from src.models.models import Order, Complaint


def create_order(customer, day):
    customer.last_active = day
    return Order()


def create_complaint(customer, day):
    customer.last_active = day
    return Complaint()
