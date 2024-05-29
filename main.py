import json
import os

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

from src.emulation.emulation import emulate_day
from src.models.models import Workshop, Employee, Base

with open("data\\parameters\\dates.json") as file:
    dates = json.load(file)

with open("data\\parameters\\employees.json", encoding='utf-8') as file:
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
Base.metadata.create_all(conn)

Session = sa.orm.sessionmaker(bind=conn)
session = Session()

date_range = pd.date_range(dates["start"], periods=10).to_pydatetime().tolist()
date_range = [d for d in date_range if d.weekday() < 5]

workshop = Workshop()
employees = [Employee(workshop, dates["start"], *employees_data[k].values()) for k in employees_data.keys()]
customers = []
orders = []

for day in date_range:
    emulate_day(day, employees, customers, orders)

session.add_all(customers)
session.add(workshop)
session.add_all(employees)
session.commit()
