import sqlalchemy as sa

class Complaint:
    __tablename__ = "complaints"
    id = sa.Column('id', sa.Integer, primary_key=True)
    employee_id = sa.Column('employee_id type', sa.Integer)
    service_id = sa.relationship("services", back_populates="id")
    open_date = sa.Column('open_date', sa.Date)
    closure_date = sa.Column('closure_date', sa.Date)
    description = sa.Column('description', sa.String(25))
    cost = sa.Column('cost', sa.DECIMAL(8, 2))

    def init(self, id, employee_id, service_id, open_date, closure_date, description, cost):
        self.id = id
        self.employee_id = employee_id
        self.service_id = service_id
        self.open_date = open_date
        self.closure_date = closure_date
        self.description = description
        self.cost = cost