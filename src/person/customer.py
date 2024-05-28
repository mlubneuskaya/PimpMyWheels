import random

from .person import Person
from ..complaint.complaint import Complaint


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.last_order = None
        self.last_active = None
        self.account_deletion_date = None

    def complains(self):
        if self.last_order == "sell":
            if random.random() < 0.01:
                return True
            return False
        if self.last_order == "buy":
            if random.random() < 0.05:
                return True
            return False
        if self.last_order == "fix":
            if random.random() < 0.1:
                return True
            return False

    def complain(self):
        return Complaint()
