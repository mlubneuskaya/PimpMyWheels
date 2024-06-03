import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.models.base import Base

class Complaint(Base):
    __tablename__ = "complaints"
    id = sa.Column('id', sa.Integer, primary_key=True)
    employee_id = sa.orm.mapped_column(sa.ForeignKey("employees.id"))
    service_id = sa.orm.mapped_column(sa.ForeignKey("services.id"))
    open_date = sa.Column('open_date', sa.Date)
    closure_date = sa.Column('closure_date', sa.Date)
    description = sa.Column('description', sa.String(25))
    cost = sa.Column('cost', sa.DECIMAL(8, 2))

    service = relationship("Services")
    employee = relationship("Employee")
    
    def init(self, employee, open_date, closure_date, description, cost, service):
        self.employee = employee
        self.open_date = open_date
        self.closure_date = closure_date
        self.description = description
        self.cost = cost
        self.service = service