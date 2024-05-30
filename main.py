import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import random
from datetime import timedelta

from src.emulation.emulation import emulate_day
from src.models.workshop import Workshop
from src.models.employee import Employee
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

open_date1 = date_range[0]
days_offset = random.randint(120, 240)  # 180 ± 60 days
open_date2 = open_date1 + timedelta(days=days_offset)

workshop = [Workshop(open_date1), Workshop(open_date2)]
employees = [Employee(workshop, date_range[0], *employees_data[k].values()) for k in employees_data.keys()]
customers = []
orders = []
services = []

for day in date_range:
    emulate_day(day, employees, customers, orders, services)

session.add_all(customers)
session.add(workshop)
session.add_all(employees)
session.add_all(services)
session.commit()
