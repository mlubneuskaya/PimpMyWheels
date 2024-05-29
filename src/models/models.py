from datetime import date

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from src.utils.generator import get_name, get_phone_number, get_surname, get_address

Base = declarative_base()


def get_base():
    return Base


class Customer(Base):
    __tablename__ = "customers"
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(50))
    surname = sa.Column('surname', sa.String(50))
    email = sa.Column('email', sa.String(50))
    phone_number = sa.Column('phone_number', sa.String(12))
    birth_date = sa.Column('birth_date', sa.Date)
    address = sa.Column('address', sa.String(50))
    account_creation_date = sa.Column('account_creation_date', sa.Date)
    account_deletion_date = sa.Column('account_deletion_date', sa.Date)
    last_active = sa.Column('last_active', sa.Date)

    def __init__(self, day):
        self.name, sex = get_name()
        self.surname = get_surname(sex)
        self.email = f"{self.name}.{self.surname}@customer.com"
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = date.today()  # TODO age
        self.account_creation_date = day
        self.account_deletion_date = None
        self.last_active = day


class Employee(Base):
    __tablename__ = "employees"
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(50))
    surname = sa.Column('surname', sa.String(50))
    email = sa.Column('email', sa.String(50))
    phone_number = sa.Column('phone_number', sa.String(12))
    birth_date = sa.Column('birth_date', sa.Date)
    address = sa.Column('address', sa.String(50))
    workshop_id = sa.orm.mapped_column(sa.ForeignKey("workshops.id"))
    position = sa.Column('position', sa.String(100))
    hire_date = sa.Column('hire_date', sa.Date)
    quit_date = sa.Column('quit_date', sa.Date)
    salary = sa.Column('salary', sa.Float(precision=2))

    workshop = sa.orm.relationship("Workshop")

    def __init__(self, workshop, day, position, salary):
        self.workshop = workshop
        self.name, sex = get_name()
        self.surname = get_surname(sex)
        self.email = f"{self.name}.{self.surname}@pimpmywheels.com"
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = date.today()  # TODO age
        self.position = position
        self.hire_date = day
        self.quit_date = None
        self.salary = salary


class Workshop(Base):
    __tablename__ = "workshops"
    id = sa.Column('id', sa.Integer, primary_key=True)
    address = sa.Column('address', sa.String(255))
    phone_number = sa.Column('phone_number', sa.String(15))
    stations_number = sa.Column('station_number', sa.Integer)
    opening_date = sa.Column('opening_date', sa.Date)
    closing_date = sa.Column('closing_date', sa.Date)  # TODO why?

    def __init__(self):
        self.address = 'address'
        self.phone_number = '111'
        self.stations_number = 0
        self.opening_date = date.today()
        self.closing_date = date.today()


class Order:
    pass


class Complaint:
    pass
