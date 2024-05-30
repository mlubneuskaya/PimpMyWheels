import sqlalchemy as sa
from src.models.generator import get_name, get_surname, get_phone_number, get_address, get_birth_date
from base import Base


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
        self.birth_date = get_birth_date(day)
        self.account_creation_date = day
        self.account_deletion_date = None
        self.last_active = day
