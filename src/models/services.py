import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import DECIMAL

from src.models.base import Base
from src.generators.personal_data_generator import get_description, get_description_date


class Services(Base):
    __tablename__ = "services"
    id = sa.Column('id', INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
    start_date = sa.Column('start_date', sa.Date, nullable=False)
    end_date = sa.Column('end_date', sa.Date)
    parts_cost = sa.Column('parts_cost', DECIMAL(precision=8, scale=2, unsigned=True), nullable=False)
    work_cost = sa.Column('work_cost', DECIMAL(precision=8, scale=2, unsigned=True), nullable=False)
    # transaction_id = sa.orm.mapped_column(sa.ForeignKey("transactions.id"))
    description = sa.Column('address', sa.String(50), nullable=False)

    employee = relationship("Employee")

    # transaction = relationship("transactions")

    def __init__(self, employee, transaction, customer):
        self.employee = employee
        self.description = get_description()[0]
        self.start_date = get_description_date(customer.account_creation_date)[0]
        self.end_date = get_description_date(customer.account_creation_date)[1]
        self.parts_cost = get_description()[1]
        self.work_cost = get_description()[2]
        # self.transaction = transaction
