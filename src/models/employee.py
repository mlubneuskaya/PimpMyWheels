import sqlalchemy as sa
from sqlalchemy.orm import relationship
from unidecode import unidecode

from src.models.base import Base
from src.generators.personal_data_generator import get_phone_number, get_address, get_birth_date, \
    get_unique_name_surname, get_salary


class Employee(Base):
    __tablename__ = "employees"
    id = sa.Column('id', sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = sa.Column('name', sa.String(25), nullable=False)
    surname = sa.Column('surname', sa.String(25), nullable=False)
    email = sa.Column('email', sa.String(60), nullable=False)
    phone_number = sa.Column('phone_number', sa.String(12), nullable=False)
    birth_date = sa.Column('birth_date', sa.Date, nullable=False)
    address = sa.Column('address', sa.String(50), nullable=False)
    workshop_id = sa.orm.mapped_column(sa.ForeignKey("workshops.id"))
    position = sa.Column('position', sa.String(100), nullable=False)
    hire_date = sa.Column('hire_date', sa.Date, nullable=False)
    resignation_date = sa.Column('resignation_date', sa.Date)
    salary = sa.Column('salary', sa.DECIMAL(8, 2), nullable=False)

    workshop = relationship("Workshop")

    def __init__(self, workshop, day, position, min_salary, avg_salary, max_salary):
        self.workshop = workshop
        self.name, self.surname = get_unique_name_surname()
        self.email = f"{unidecode(self.name)}.{unidecode(self.surname)}@pimpmywheels.com"
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = get_birth_date(day)
        self.position = position
        self.hire_date = day
        self.resignation_date = None
        self.min_salary = min_salary
        self.avg_salary = avg_salary
        self.max_salary = max_salary
        self.salary = get_salary(min_salary, avg_salary, max_salary)
