import random

import numpy as np

from .person import Person


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.last_order = None

    def order(self):
        order = np.random.choice(["fix", "sell", "buy"], p=[.7, .1, .2])
        self.last_order = order
        return order

    def complain(self):
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
