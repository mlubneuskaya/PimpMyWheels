import random

from src.models.employee import Employee
from src.models.service import Service
from src.models.transaction import Transaction, TransactionMethod, TransactionTypes
from src.models.vehicle import Vehicle
from src.models.workshop import Workshop


class WorkshopDecisionMaker:
    order_types = ["repair", "buy", "sell"]  # meaning customer's decision

    def __init__(
        self,
        date,
        manager_salary,
        mechanics_salary,
        service_completion_probability,
        purchase_probability,
        selling_probability,
        repair_probability,
        service_parameters,
        employee_resignation_probability,
        margin,
    ):
        self.workshop = Workshop(date)
        self.manager = Employee(self.workshop, date, "MENADŻER", **manager_salary)
        self.mechanics = [
            Employee(self.workshop, date, "MECHANIK", **mechanics_salary)
            for _ in range(self.workshop.stations_number)
        ]
        self.service_completion_probability = service_completion_probability
        self.repair_probability = repair_probability
        self.purchase_probability = purchase_probability
        self.selling_probability = selling_probability
        self.margin = margin
        self.repairs = []
        self.active_repairs = []
        self.vehicles = []
        self.vehicles_in_stock = []
        self.service_parameters = service_parameters
        self.current_employees = [self.manager] + self.mechanics
        self.employees = [self.manager] + self.mechanics
        self.employee_resignation_probability = employee_resignation_probability

    def add_service_and_create_transaction(self, date, customer):
        if not self.vehicles_in_stock:
            prob_sum = self.repair_probability + self.selling_probability
            order_probabilities = [
                self.repair_probability / prob_sum,
                0,
                self.selling_probability / prob_sum,
            ]
        else:
            order_probabilities = [
                self.repair_probability,
                self.purchase_probability,
                self.selling_probability,
            ]
        order_type = random.choices(
            WorkshopDecisionMaker.order_types, weights=order_probabilities, k=1
        )[0]
        if order_type == "repair":
            vehicle = Vehicle(
                purchase=None, workshop=self.workshop, brand="Ferrari", sale=None
            )
            service_details = self.get_service_details()
            transaction = Transaction(
                transaction_method=random.choices(
                    list(TransactionMethod), weights=[0.2, 0.8]
                )[0],
                sender=customer,
                date=date,
                transaction_type=TransactionTypes["income"],
                value=(service_details["work_cost"] + service_details["part_cost"])
                * (1 + self.margin),
            )
            service = Service(
                date=date,
                employee=random.choice(self.mechanics),
                vehicle=vehicle,
                service_type=service_details["name"],
                work_cost=service_details["work_cost"],
            )
            service.transaction = transaction
            self.active_repairs.append(service)
            self.repairs.append(service)
            return transaction
        elif order_type == "buy":  # TODO ceny i marki
            transaction = Transaction(
                transaction_method=TransactionMethod["card"],
                sender=customer,
                date=date,
                transaction_type=TransactionTypes["income"],
                value=10000,
            )
            service_details = self.get_service_details()
            vehicle = random.choice(self.vehicles_in_stock)
            vehicle.sale = transaction
            self.vehicles_in_stock.remove(vehicle)
            service = Service(
                date=date,
                employee=random.choice(self.mechanics),
                vehicle=vehicle,
                service_type=service_details["name"],
                work_cost=service_details["work_cost"],
            )
            self.active_repairs.append(service)
            self.repairs.append(service)
            return transaction
        else:  # TODO ceny i marki
            transaction = Transaction(
                transaction_method=TransactionMethod["card"],
                sender=customer,
                date=date,
                transaction_type=TransactionTypes["cost"],
                value=5000,
            )
            vehicle = Vehicle(
                purchase=transaction, workshop=self.workshop, brand="Bugatti", sale=None
            )
            self.vehicles.append(vehicle)
            self.vehicles_in_stock.append(vehicle)
            return transaction

    def complete_repairs(self, date):
        for repair in self.active_repairs:
            if random.random() < self.service_completion_probability:
                repair.end_date = date
                self.active_repairs.remove(repair)

    def employee_turnover(self, date):
        for employee in self.current_employees:
            if random.random() < self.employee_resignation_probability:
                employee.resignation_date = date
                new_employee = Employee(
                    workshop=employee.workshop,
                    day=date,
                    position=employee.position,
                    min_salary=employee.min_salary,
                    avg_salary=employee.avg_salary,
                    max_salary=employee.max_salary,
                )
                self.employees.append(new_employee)
                self.current_employees.append(new_employee)

    def get_service_details(self):
        probabilities = [desc["probability"] for desc in self.service_parameters]
        description = random.choices(
            self.service_parameters, weights=probabilities, k=1
        )[0]
        return description
