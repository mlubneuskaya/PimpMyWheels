import sqlalchemy as sa
from unidecode import unidecode

from src.models.base import Base
from src.models.personal_data_generator import get_phone_number, get_address, get_birth_date, get_unique_name_surname


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

    def __init__(self, date):
        self.name, self.surname = get_unique_name_surname()
        self.email = f"{unidecode(self.name)}.{unidecode(self.surname)}@customer.com"
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = get_birth_date(date)
        self.account_creation_date = date
        self.account_deletion_date = None
        self.last_active = date
