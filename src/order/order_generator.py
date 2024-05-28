import numpy as np

from src.order.order import Order


class RandomOrderGenerator:
    def __init(self, probabilities):
        self.p = probabilities

    def create_order(self, customer):
        if not customer.account_deletion_date:
            order = np.random.choice(["fix", "sell", "buy"], p=self.p)
            customer.last_order = order
            return Order()
        return None
