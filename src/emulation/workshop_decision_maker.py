import random

from src.models.employee import Employee
from src.models.service import Service
from src.models.transaction import Transaction, TransactionMethod, TransactionTypes
from src.models.workshop import Workshop


class WorkshopDecisionMaker:
    order_types = ["repair", "buy", "sell"]

    def __init__(self,
                 date,
                 manager_salary,
                 mechanics_salary,
                 service_completion_probability,
                 purchase_probability,
                 selling_probability,
                 repair_probability,
                 service_parameters,
                 employee_resignation_probability):
        self.workshop = Workshop(date)
        self.manager = Employee(self.workshop,
                                date,
                                "MENADŻER",
                                **manager_salary)
        self.mechanics = [Employee(self.workshop,
                                   date,
                                   "MECHANIK",
                                   **mechanics_salary) for _ in range(self.workshop.stations_number)]
        self.service_completion_probability = service_completion_probability
        self.order_probabilities = [repair_probability, purchase_probability, selling_probability]
        self.repairs = []
        self.active_repairs = []
        self.vehicles = []
        self.service_parameters = service_parameters
        self.current_employees = [self.manager] + self.mechanics
        self.employees = [self.manager] + self.mechanics
        self.employee_resignation_probability = employee_resignation_probability

    def add_service_and_create_transaction(self, date, customer):
        order_type = random.choices(WorkshopDecisionMaker.order_types, weights=self.order_probabilities, k=1)[0]
        if order_type == "repair":
            transaction = Transaction(transaction_method=random.choices(list(TransactionMethod), weights=[0.2, 0.8])[0],
                                      sender=customer,
                                      date=date,
                                      transaction_type=TransactionTypes['income'],
                                      value=500)
            service_details = self.get_service_details()
            service = Service(date=date,
                              employee=random.choice(self.mechanics),
                              service_type=service_details['name'],
                              work_cost=service_details['work_cost'])
            service.transaction = transaction
            self.active_repairs.append(service)
            self.repairs.append(service)
            return transaction
        if order_type == "buy":
            pass
        if order_type == "sell":
            pass

    def complete_repairs(self, date):
        for repair in self.active_repairs:
            if random.random() < self.service_completion_probability:
                repair.end_date = date
                self.active_repairs.remove(repair)

    def employee_turnover(self, date):
        for employee in self.current_employees:
            if random.random() < self.employee_resignation_probability:
                employee.resignation_date = date
                new_employee = Employee(workshop=employee.workshop,
                                        day=date,
                                        position=employee.position,
                                        min_salary=employee.min_salary,
                                        avg_salary=employee.avg_salary,
                                        max_salary=employee.max_salary)
                self.employees.append(new_employee)
                self.current_employees.append(new_employee)

    def get_service_details(self):
        probabilities = [desc['probability'] for desc in self.service_parameters]
        description = random.choices(self.service_parameters, weights=probabilities, k=1)[0]
        return description
