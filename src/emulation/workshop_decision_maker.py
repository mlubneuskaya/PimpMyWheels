import random

from src.models.employee import Employee


class WorkshopDecisionMaker:
    order_types = ["repair", "buy", "sell"]

    def __init__(
        self,
        manager_salary,
        mechanics_salary,
        service_completion_probability,
        purchase_probability,
        selling_probability,
        repair_completion_probability,
        service_parameters,
        employee_resignation_probability,
    ):
        self.manager_salary = manager_salary
        self.mechanics_salary = mechanics_salary
        self.service_completion_probability = service_completion_probability
        self.repair_completion_probability = repair_completion_probability
        self.purchase_probability = purchase_probability
        self.selling_probability = selling_probability
        self.service_parameters = service_parameters
        self.employee_resignation_probability = employee_resignation_probability

    def create_manager(self, workshop, date):
        return Employee(workshop, date, "MENADŻER", **self.manager_salary)

    def create_mechanic(self, workshop, date):
        return Employee(workshop, date, "MECHANIK", **self.mechanics_salary)

    def choose_order_type(self, vehicles_in_stock):
        if not vehicles_in_stock:
            repair_selling_probability = (
                self.repair_completion_probability + self.selling_probability
            )
            order_probabilities = [
                self.repair_completion_probability / repair_selling_probability,
                0,
                self.selling_probability / repair_selling_probability,
            ]
        else:
            order_probabilities = [
                self.repair_completion_probability,
                self.purchase_probability,
                self.selling_probability,
            ]
        order_type = random.choices(
            WorkshopDecisionMaker.order_types, weights=order_probabilities, k=1
        )[0]
        return order_type

    def choose_repairs_to_complete(self, date, repairs):
        repairs_to_complete = []
        for repair in repairs:
            if random.random() < self.service_completion_probability:
                repairs_to_complete.append(repair)
        return repairs_to_complete
