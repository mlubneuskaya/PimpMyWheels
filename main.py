import json
import os
from datetime import date

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

from src.models.models import Workshop, Employee, Customer

with open("data\\parameters\\dates.json") as file:
    dates = json.load(file)

with open("data\\parameters\\employees.json") as file:
    employees_data = json.load(file)


date_range = pd.date_range(dates["start"], periods=dates["length"]).to_pydatetime().tolist()
date_range = [d for d in date_range if d.weekday() < 5]

load_dotenv()
url_object = sa.URL.create(
    drivername="mariadb+mariadbconnector",
    host="giniewicz.it",
    username=os.getenv('LOGIN'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('BASE')
)

conn = sa.create_engine(url_object)
Session = sa.orm.sessionmaker(bind=conn)
session = Session()

workshop1 = Workshop()

employees = [Employee(workshop1, date.today(), *employees_data[k].values()) for k in employees_data.keys()]

customers = [Customer(date.today()), Customer(date.today())]

session.add_all(customers)
session.add(workshop1)
session.add_all(employees)
session.commit()
