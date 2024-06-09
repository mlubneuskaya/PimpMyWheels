import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.models.base import Base
from src.generators.personal_data_generator import get_description, get_description_date


class Services(Base):
    __tablename__ = "services"
    id = sa.Column('id', sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
    start_date = sa.Column('start_date', sa.Date, nullable=False)
    end_date = sa.Column('end_date', sa.Date, nullable=False)
    parts_cost = sa.Column('parts_cost', sa.DECIMAL(8, 2), nullable=False)
    work_cost = sa.Column('work_cost', sa.DECIMAL(8, 2), nullable=False)
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
