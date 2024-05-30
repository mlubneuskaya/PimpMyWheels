import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.models.base import Base
from src.models.generator import get_name, get_surname, get_phone_number, get_address, get_birth_date


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
    resignation_date = sa.Column('resignation_date', sa.Date)
    salary = sa.Column('salary', sa.Float(precision=2))

    workshop = relationship("Workshop")

    def __init__(self, workshop, day, position, salary):
        self.workshop = workshop
        self.name, sex = get_name()
        self.surname = get_surname(sex)
        self.email = f"{self.name}.{self.surname}@pimpmywheels.com"
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = get_birth_date(day)
        self.position = position
        self.hire_date = day
        self.resignation_date = None
        self.salary = salary
