import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.models.customer import Customer

from src.models.personal_data_generator import get_description, get_description_date


class Services:
    __tablename__ = "services"
    id = sa.Column('id', sa.Integer, primary_key=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
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
        self.start_date = get_description_date(Customer.account_creation_date)[0]
        self.end_date = get_description_date(Customer.account_creation_date)[1]
        self.parts_cost = get_description()[1]
        self.work_cost = get_description()[2]
        self.transaction = transaction
