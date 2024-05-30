from sqlalchemy.orm import relationship

from src.models.base import Base
import sqlalchemy as sa


class Equipment(Base):
    __tablename__ = "equipment"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True, comment="Id wyposażenia")
    name = sa.Column(sa.String(255), nullable=False, comment="Nazwa")
    type = sa.Column(sa.String(50), nullable=False, comment="Typ")
    number_in_stock = sa.Column(sa.Integer, nullable=False, comment="Ilość na stanie")
    facility_id = sa.Column(sa.Integer, sa.ForeignKey("facilities.id"), nullable=False, comment="Id placówki")

    facility = relationship("Facility")

    def __init__(self, name, type, number_in_stock, facility_id):
        self.name = name
        self.type = type
        self.number_in_stock = number_in_stock
        self.facility_id = facility_id
