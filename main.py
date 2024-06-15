import json
import os

from src.emulation.customer_decision_maker import CustomerDecisionMaker
from src.generators.objects_generator import create_employees

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

from src.emulation.emulation import emulate_day
from src.models.workshop import Workshop
from src.models.base import Base

with open(r"data\parameters\dates.json") as file:
    dates = json.load(file)

with open(r"data\parameters\employees.json", encoding='utf-8') as file:
    employees_data = json.load(file)

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

open_date = date_range[0]
# days_offset = random.randint(120, 240)  # 180 ± 60 days
# open_date2 = open_date1  # + timedelta(days=days_offset)

workshops = [Workshop(open_date), Workshop(open_date)]
positions = [['manager'] + ['mechanic'] * workshop.stations_number for workshop in workshops]
employees = sum([create_employees(workshop, pos, employees_data, date_range[0])
                 for workshop, pos in zip(workshops, positions)], [])

orders = []
complaints = []

customer_decision_maker = CustomerDecisionMaker(account_deactivation_probability=0.01,
                                                purchase_probability=0.2,
                                                selling_probability=0.2,
                                                repair_probability=0.6,
                                                regular_customers_per_day=0.01,
                                                new_customers_per_day=4)

for date in date_range:
    emulate_day(date, employees, customer_decision_maker, orders, complaints)

session.add_all(customer_decision_maker.all_customers)
session.add_all(workshops)
session.add_all(orders)
session.add_all(employees)
session.commit()
