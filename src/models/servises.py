import sqlalchemy as sa
from sqlalchemy.orm import relationship
from unidecode import unidecode

from src.models.base import Base
from src.models.customer import Customer

from datetime import timedelta
import random

from generat import get_description


class Servises:
    __tablename__ = "serwices"
    id = sa.Column('id', sa.Integer, primary_key=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("Employees.id"))
    start_date = sa.Column('start_date', sa.Date)
    end_date = sa.Column('end_date', sa.Date)
    parts_cost = sa.Column('parts_cost', sa.Float(precision=2))
    work_cost = sa.Column('work_cost', sa.Float(precision=2))
    transaction_id = sa.orm.mapped_column(sa.ForeignKey("transactions.id"))
    description = sa.Column('address', sa.Text)

    employee = relationship("employees")
    transaction = relationship("transactions")
    
    def __init__(self, employee, transaction):
        self.employee = employee
        self.description = get_description()[0]
        self.start_date = self.generate_start_date(Customer.account_creation_date)
        self.end_date = self.generate_end_date(self.start_date)
        self.parts_cost = get_description()[1]
        self.work_cost = get_description()[2]
        self.transaction = transaction
        
    def generate_start_date(self, account_creation_date):
        start = account_creation_date
        end = account_creation_date + timedelta(days=60)
        return start + timedelta(days=random.randint(1, (end - start).days))
    
    def generate_end_date(self, start_date):
        if random.choice([True, False]):
            return start_date + timedelta(days=random.randint(1, 30))
        else:
            return None
