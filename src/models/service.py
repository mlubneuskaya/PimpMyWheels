import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import DECIMAL

from src.models.base import Base


class Service(Base):
    __tablename__ = "services"
    id = sa.Column('id', INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
    start_date = sa.Column('start_date', sa.Date, nullable=False)
    end_date = sa.Column('end_date', sa.Date, nullable=True)
    work_cost = sa.Column('work_cost', DECIMAL(precision=8, scale=2, unsigned=True), nullable=False)
    transaction_id = sa.orm.mapped_column(sa.ForeignKey("transactions.id"), nullable=True)
    description = sa.Column('description', sa.String(100), nullable=False)
    vehicle_id = sa.orm.mapped_column(sa.ForeignKey("vehicles.id"))

    employee = relationship("Employee", foreign_keys=[employee_id])
    transaction = relationship("Transaction", foreign_keys=[transaction_id])
    vehicle = relationship("Vehicle", foreign_keys=[vehicle_id])

    def __init__(self, date, employee, vehicle, service_type, work_cost, transaction=None):
        self.transaction = transaction
        self.employee = employee
        self.vehicle = vehicle
        self.description = service_type
        self.start_date = date
        self.end_date = None
        self.work_cost = work_cost

