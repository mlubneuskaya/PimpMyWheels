import random

from src.emulation.workshop_decision_maker import WorkshopDecisionMaker
from src.models.service import Service
from src.models.transaction import Transaction, TransactionMethod, TransactionTypes
from src.models.vehicle import Vehicle
from src.models.workshop import Workshop


class WorkshopEmulator:
    def __init__(
        self,
        date,
        decision_maker: WorkshopDecisionMaker,
        service_parameters,
        employee_resignation_probability,
        margin,
    ):
        self.decision_maker = decision_maker
        self.workshop = Workshop(date)
        self.manager = decision_maker.create_manager(self.workshop, date)
        self.mechanics = [
            self.decision_maker.create_mechanic(self.workshop, date)
            for _ in range(self.workshop.stations_number)
        ]
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
        order_type = self.decision_maker.choose_order_type(self.vehicles_in_stock)
        if order_type == "repair":
            return self.create_repair_service(date, customer)
        elif order_type == "buy":  # TODO ceny i marki
            return self.buy_vehicle(date, customer)
        else:  # TODO ceny i marki
            return self.sell_vehicle(date, customer)

    def create_repair_service(self, date, customer):
        vehicle = Vehicle(
            purchase=None, workshop=self.workshop, brand="Ferrari", sale=None
        )
        service = Service(
            date=date,
            employee=random.choice(self.mechanics),
            vehicle=vehicle,
            service_parameters=self.service_parameters,
        )
        transaction = Transaction(
            transaction_method=random.choices(
                list(TransactionMethod), weights=[0.2, 0.8]
            )[0],
            sender=customer,
            date=date,
            transaction_type=TransactionTypes["income"],
            value=(service.work_cost + service.part_cost) * (1 + self.margin),
        )
        service.transaction = transaction
        self.active_repairs.append(service)
        self.repairs.append(service)
        return transaction

    def buy_vehicle(self, date, customer):
        transaction = Transaction(
            transaction_method=TransactionMethod["card"],
            sender=customer,
            date=date,
            transaction_type=TransactionTypes["income"],
            value=10000,
        )
        vehicle = random.choice(self.vehicles_in_stock)
        vehicle.sale = transaction
        self.vehicles_in_stock.remove(vehicle)
        service = Service(
            date=date,
            employee=random.choice(self.mechanics),
            vehicle=vehicle,
            service_parameters=self.service_parameters,
        )
        self.active_repairs.append(service)
        self.repairs.append(service)
        return transaction

    def sell_vehicle(self, date, customer):
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
        repairs_to_complete = self.decision_maker.choose_repairs_to_complete(
            date, self.active_repairs
        )
        self.active_repairs = [
            repair
            for repair in self.active_repairs
            if repair not in repairs_to_complete
        ]

    def employee_turnover(self, date):
        for employee in self.current_employees:
            if random.random() < self.employee_resignation_probability:
                employee.resignation_date = date
                if employee.position == "MENADŻER":
                    new_employee = self.decision_maker.create_manager(
                        self.workshop, date
                    )
                else:
                    new_employee = self.decision_maker.create_mechanic(
                        self.workshop, date
                    )
                self.employees.append(new_employee)
                self.current_employees.append(new_employee)
