import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import DECIMAL

from src.models.base import Base


class Complaint(Base):
    __tablename__ = "complaints"
    id = sa.Column(
        "id",
        INTEGER(unsigned=True),
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
    service_id = sa.orm.mapped_column(sa.ForeignKey("services.id"))
    open_date = sa.Column("open_date", sa.Date, nullable=False)
    closure_date = sa.Column("closure_date", sa.Date, nullable=False)
    description = sa.Column("description", sa.String(25), nullable=False)
    cost = sa.Column(
        "cost", DECIMAL(precision=8, scale=2, unsigned=True), nullable=False
    )

    service = relationship("Service")
    employee = relationship("Employee")

    def __init__(self, employee, service, open_date, closure_date, description, cost):
        self.employee = employee
        self.service = service
        self.open_date = open_date
        self.closure_date = closure_date
        self.description = description
        self.cost = cost
