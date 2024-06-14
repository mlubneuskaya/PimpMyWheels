import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

from src.models.base import Base


class Inventory(Base):
    __tablename__ = "inventory"
    id = sa.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True, comment="Id inwentarza")
    equipment_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey('equipment.id'), nullable=False, comment="Id wyposażenia")
    service_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey('services.id'), nullable=False, comment="Id usługi")
    workshop_id = sa.Column(INTEGER(unsigned=True), sa.ForeignKey('workshops.id'), nullable=False, comment="Id warsztatu")

    equipment = relationship("Equipment", back_populates="inventories")
    service = relationship("Service")
    workshop = relationship("Workshop")

    def __init__(self, equipment_id, service_id, workshop_id):
        self.equipment_id = equipment_id
        self.service_id = service_id
        self.workshop_id = workshop_id
