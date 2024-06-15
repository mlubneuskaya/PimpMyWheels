import json
import os

from src.emulation.customer_decision_maker import CustomerDecisionMaker
from src.emulation.workshop_decision_maker import WorkshopDecisionMaker

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

from src.emulation.emulation import emulate_day
from src.models.base import Base

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(r"data\parameters\dates.json") as file:
    dates = json.load(file)

with open(r"data\parameters\employees.json", encoding='utf-8') as file:
    employees_data = json.load(file)

with open("data\\parameters\\services_parts.json", "r", encoding="utf-8") as file:
    service_parameters = json.load(file)

load_dotenv()
url_object = sa.URL.create(
    drivername="mariadb+mariadbconnector",
    host="giniewicz.it",
    username=os.getenv('LOGIN'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('BASE')
)

conn = sa.create_engine(url_object)

Base.metadata.drop_all(conn)
Base.metadata.create_all(conn)

Session = sa.orm.sessionmaker(bind=conn)
session = Session()

date_range = pd.date_range(dates["start"], periods=10).to_pydatetime()  # .tolist()
date_range = [d for d in date_range if d.weekday() < 5]


workshop_decision_maker1 = WorkshopDecisionMaker(date=date_range[0],
                                                 manager_salary=employees_data['manager'],
                                                 mechanics_salary=employees_data['mechanic'],
                                                 service_completion_probability=0.9,
                                                 purchase_probability=0.2,
                                                 selling_probability=0.2,
                                                 repair_probability=0.6,
                                                 service_parameters=service_parameters,
                                                 employee_resignation_probability=1/365,
                                                 margin=0.2)

workshop_decision_maker2 = WorkshopDecisionMaker(date=date_range[0],
                                                 manager_salary=employees_data['manager'],
                                                 mechanics_salary=employees_data['mechanic'],
                                                 service_completion_probability=0.7,
                                                 purchase_probability=0.2,
                                                 selling_probability=0.2,
                                                 repair_probability=0.6,
                                                 service_parameters=service_parameters,
                                                 employee_resignation_probability=2/365,
                                                 margin=0.2)


workshop_decision_makers = [workshop_decision_maker1, workshop_decision_maker2]
customer_decision_maker = CustomerDecisionMaker(account_deactivation_probability=0.01,
                                                regular_customers_per_day=0.1,
                                                new_customers_per_day=4)

complaints = []
transactions = []

for date in date_range:
    emulate_day(date, workshop_decision_makers, customer_decision_maker, transactions)

workshops = [wdm.workshop for wdm in workshop_decision_makers]
employees = sorted(
    [emp for wdm in workshop_decision_makers
     for emp in wdm.employees],
    key=lambda x: x.hire_date)
services = sorted(
    [service for wdm in workshop_decision_makers
     for service in wdm.repairs],
    key=lambda x: x.start_date)
vehicles = sorted(
    [vehicle for wdm in workshop_decision_makers
     for vehicle in wdm.vehicles],
    key=lambda x: x.purchase.date)

session.add_all(customer_decision_maker.all_customers)
session.add_all(workshops)
session.add_all(employees)
session.add_all(transactions)
session.add_all(services)
session.add_all(vehicles)
session.commit()
