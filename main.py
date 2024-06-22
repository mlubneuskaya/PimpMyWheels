import json
import os

from src.emulation.customer_decision_maker import CustomerDecisionMaker
from src.emulation.equipment_generator import generate_equipment_table
from src.emulation.workshop_decision_maker import WorkshopDecisionMaker
from src.emulation.workshop_emulator import WorkshopEmulator

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

from src.emulation.emulation import emulate_day
from src.models.base import Base

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(r"data\parameters\dates.json") as file:
    dates = json.load(file)

with open(r"data\parameters\employees.json", encoding="utf-8") as file:
    employees_data = json.load(file)

with open("data\\parameters\\services_parts.json", "r", encoding="utf-8") as file:
    service_parameters = json.load(file)

load_dotenv()
url_object = sa.URL.create(
    drivername="mariadb+mariadbconnector",
    host="giniewicz.it",
    username=os.getenv("LOGIN"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("BASE"),
)

conn = sa.create_engine(url_object)

Base.metadata.drop_all(conn)
Base.metadata.create_all(conn)

Session = sa.orm.sessionmaker(bind=conn)
session = Session()

date_range = pd.date_range(dates["start"], periods=30).to_pydatetime()
date_range = [d for d in date_range if d.weekday() < 5]

equipment = generate_equipment_table(service_parameters=service_parameters)

workshop_decision_maker1 = WorkshopDecisionMaker(
    manager_salary=employees_data["manager"],
    mechanics_salary=employees_data["mechanic"],
    purchase_probability=0.3,
    selling_probability=0.15,
    repair_completion_probability=0.4,
    service_parameters=service_parameters,
    employee_resignation_probability=1 / (365 * 2),
    number_of_items_in_stock=10,
)

workshop_emulator1 = WorkshopEmulator(
    date=date_range[0],
    decision_maker=workshop_decision_maker1,
    service_parameters=service_parameters,
    margin=0.2,
    equipment=equipment,
)

workshop_decision_maker2 = WorkshopDecisionMaker(
    manager_salary=employees_data["manager"],
    mechanics_salary=employees_data["mechanic"],
    purchase_probability=0.2,
    selling_probability=0.2,
    repair_completion_probability=0.3,
    service_parameters=service_parameters,
    employee_resignation_probability=1 / 365,
    number_of_items_in_stock=10,
)

workshop_emulator2 = WorkshopEmulator(
    date=date_range[0],
    decision_maker=workshop_decision_maker2,
    service_parameters=service_parameters,
    margin=0.2,
    equipment=equipment,
)

workshop_emulators = [workshop_emulator1, workshop_emulator2]
customer_decision_maker = CustomerDecisionMaker(
    account_deactivation_probability=0.01,
    regular_customers_per_day=0.1,
    new_customers_per_day=4,
)

complaints = []
transactions = []

for day_number, date in enumerate(date_range):
    emulate_day(
        date, workshop_emulators, customer_decision_maker, transactions, day_number
    )

workshops = [wdm.workshop for wdm in workshop_emulators]
employees = sorted(
    [emp for wdm in workshop_emulators for emp in wdm.employees],
    key=lambda x: x.hire_date,
)
services = sorted(
    [service for wdm in workshop_emulators for service in wdm.repairs],
    key=lambda x: x.start_date,
)

vehicles = sorted(
    [vehicle for wdm in workshop_emulators for vehicle in wdm.vehicles],
    key=lambda x: x.purchase.date,
)

inventory = sorted(
    [inv for wdm in workshop_emulators for inv in wdm.inventory],
    key=lambda x: x.delivery_date,
)

session.add_all(equipment)
session.add_all(customer_decision_maker.all_customers)
session.add_all(workshops)
session.add_all(employees)
session.add_all(transactions)
session.add_all(services)
session.add_all(vehicles)
session.add_all(inventory)
session.commit()
